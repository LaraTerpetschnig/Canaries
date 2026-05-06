# Data Cleaning
## Year Filtering (2019)

Filters the raw Meal Gap Excel file  to keep only rows where `Year == 2019`.

```python
mmg_2019 = mmg_raw[mmg_raw['Year'] == 2019].copy()
```
The Food Access Resreach Atlas (FARA) dataset combines data from multiple collection years including urban/rural flags from 2019, Census counts from 2010, and income/SNAP figures from the 2014–2018 American Community Survey. To minimize time inconsistenies between the datasets, the Map the Meal Gap(MMG) data is cleaned to include only 2019.

---

## County Name Extraction
Parses the `County, State` string field (for example `"Autauga County, Alabama"`) by splitting on `", "` and keeping the first token, creating a standalone `County` column.

```python
mmg_2019['County'] = mmg_2019['County, State'].str.split(', ').str[0]
```
A combined `County, State` field cannot be used directly for county-level display for visualizations. Splitting it produces clean county values consistent with the `County` and `State` columns present in the FARA dataset.

## Column Renaming
Renames 17 verbosely labelled MMG columns to shorter, standardized camelCase names using a mapping dictionary.

```python
column_mapping = {
    'Overall Food Insecurity Rate': 'pctFoodInsecure',
    '# of Food Insecure Persons Overall': 'numFoodInsecure',
    # ... (additional columns)
}
mmg_2019 = mmg_2019.rename(columns=column_mapping)
```
Original column names contain special characters (`≤`, `%`, `#`), and inconsistent formatting. Standardized names make referencing columns consistent in the merged dataset.

## Column Selection
Retains the 20 relevant columns from the renamed MMG dataframe, dropping  other columns.

```python
final_columns = [
    'FIPS', 'State', 'County', 'pctFoodInsecure', 
    # ... (additional columns)
]
meal_gap = mmg_2019[final_columns]
```

 Selecting only these columns eliminates extra MMG columns not needed for analysis and reduces the chance of introducing incomplete or uninformative data into the merged dataset.

---

## FIPS Code Standardization (Zero-Padding)
Ensures FIPS codes are fixed strings with leading zeros, and gets a 5-digit county FIPS key from the 11-digit FARA census tract column.

```python
mmg['FIPS'] = mmg['FIPS'].astype(str).str.zfill(5)
fara['CensusTract'] = fara['CensusTract'].astype(str).str.zfill(11)
fara['county_fips'] = fara['CensusTract'].str[:5]
```
Without zero-padding, join keys between the two datasets would fail for any county in states with a leading-zero state code (01–09).

---

## Census Tract to County Aggregation
Aggergates the tract-level FARA data (72,864 rows) to county level (3,142 rows).

- **Sum** for count columns (population, housing unit, access-zone counts, and flags), using `min_count=1` to return `NaN` rather than `0` when all tracts are missing.
- **Mean** for rate and percentage,columns(`PovertyRate`, `MedianFamilyIncome`, `PCTGQTRS`).

```python
county = fara.groupby('county_fips')[sum_cols].sum(min_count=1)
```

---

## Left Merge on FIPS
Joins the 20-column county-level MMG dataset to the FARA county-level dataset on matching FIPS codes using a left join.

```python
merged = mmg.merge(county, left_on='FIPS', right_on='county_fips', how='left')
```
`meal_gap_data_quality.ipynb` checks that MMG contains exactly 3,142 unique FIPS codes with no duplicates. `food_atlas_data_quality.ipynb` checks that FARA's `CensusTract` field is complete, so the derived `county_fips` column is reliable. The left join strategy ensures that every county is retained in the output.

---

## Cleaning Numerical Columns

Removes `%` characters from ten percentage-valued columns.

```python
def strip_pct(series, dtype):
    if series.dtype == object:
        return series.str.replace('%', '').astype(dtype)
    return series.astype(dtype)

merged['pctFoodInsecure'] = strip_pct(merged['pctFoodInsecure'], 'float')
# ... applied to additional percent columns
```
Strips commas from two integer count columns.

```python
merged['numFoodInsecure'] = merged['numFoodInsecure'].apply(
    lambda x: int(float(str(x).replace(",", ""))) if pd.notna(x) else x)
merged['numKidsFoodInsecure'] = merged['numKidsFoodInsecure'].apply(
    lambda x: int(float(str(x).replace(",", ""))) if pd.notna(x) else x)
```
Removes `$` symbols (and commas) from three cost/budget columns and converts them to numeric types.

```python
def strip_dollar(series, dtype):
    if series.dtype == object:
        return series.str.replace('$', '').astype(dtype)
    return series.astype(dtype)
```
Cleaning these numerical columns will allow for creating visualizations and data analysis. 

