# Title: Urban & Rural Divides in U.S. Food Insecurity

# Contributors: Lily Rybka, Lara Terpetschnig

# Summary: []

# Data profiles: 

## Food Atlas (FARA) Data Profile

### Structure

The Food Access Research Atlas is avalible as a single Microsoft Excel file (`.xlsx`), with the 2019 edition weighing approximately 81.8 MB. Each row corresponds to a single U.S. Census tract, identified by a FIPS code. The 2010 Census tract geography serves is the spatial base for the data, so that when used in GIS (such as python's Geopandas and shapefiles), the spreadsheet must be joined to a 2010 tract boundary file. The columns contain attributes that can be grouped into catagories:

- **Identifiers & geography** – tract ID, state, county, and urban/rural status.
- **Demographics** – total population, number of housing units, poverty rate, median family income, low-income tract flag.
- **Food-access distance measures** – multiple binary flags and population counts that indicate whether the tract qualifies as low-income *and* low-access (formerly, “food deserts”) at combinations of ½‑mile, 1‑mile, 10‑mile, and 20‑mile thresholds, plus a vehicle‑access‑adjusted measure.
- **Sub‑population access indicators** – examples: number/percentage of children, seniors, low‑income individuals, and households without a vehicle who live far from a supermarket.

The `.zip` foler also includes a **data dictionary** sheet that defines every variable. Previous versions (2015, 2010) and the archived “Food Desert Locator” (2006) are also available as `.zip` downloads.

---
### Content 
**Demographic and Economic Variables**

| Variable | Definition | Source |
|----------|------------|--------|
| `Pop2010` | Total number of persons residing in the tract (2010 U.S. Census). | 2010 U.S. Census block level data |
| `Housing2010` | Total housing units in the tract. | 2010 U.S. Census block level data |
| `PovertyRate` | Share of tract population with income ≤ federal poverty thresholds. | 2014‑2018 American Community Survey (ACS) 5‑year estimates |
| `MedianFamilyIncome` | Median family income of the tract (including families with zero income). | 2014‑2018 ACS |
| `LowIncomeTracts` | Binary flag (1/0) indicating whether the tract meets the NMTC low‑income definition (poverty ≥20 % OR median family income ≤80 % of state/metro median). | Department of Treasury’s New Markets Tax Credit (NMTC) program |
| `Urban` / `Rural` | Status based on the population‑weighted centroid. Urban if >2,500 people or otherwise rural. | Bureau of the Census urbanized area definitions |

**Food‑access Distance Measures**

The Atlas includes four low‑income‑and‑low‑access (LILA) definitions that have a  binary flag and supporting population counts and shares:

- **Half‑mile/10‑mile**: urban tracts are measured at ½‑mile, rural at 10‑miles.  
   *Flags:* `LILATracts_halfAnd10`, `LAhalfAnd10`, etc..

- **1‑mile/10‑mile**: urban 1‑mile, rural 10‑miles.  
   *Flags:* `LILATracts_1And10`, `LA1And10`, etc..

- **1‑mile/20‑mile**: urban 1‑mile, rural 20‑miles.  
   *Flags:* `LILATracts_1And20`, `LA1And20`, etc..

- **Vehicle‑access measure**: low‑income tracts where ≥100 households are >½‑mile from a supermarket *and* lack a vehicle, OR ≥500 persons (or 33 % of the population) live >20 miles from a supermarket regardless of vehicle access.  
   *Flags:* `LILATracts_vehicle`, `LAvehicle`, etc..

For each measure the Atlas reports the total number of people and the share of the tract population that is beyond the distance threshold. It also reports the same types of counts for children, seniors, low‑income individuals, and zero‑vehicle households.

---

### Characteristics

- **Geography**: A Census tract isthe smallest level that consistent food‑access indicators are publicly available. This allows intra‑county analysis. However, the other dataset used in this project does not includedata for any area smaller than a county, so it will not be used in this project.
- **Timeliness**: The current version uses 2019 store data, 2010 Census populations, and 2014‑2018 ACS income data. The Atlas is updated periodically. 
- **Urban/rural**: Urban/rural status is assigned based on the tract’s population‑weighted centroid using the Census Bureau’s urbanized‑area definition (<2,500 = rural). Because distance thresholds differ for urban vs. rural tracts, the Atlas accounts for rural residents having to travel farther to reach a supermarket.
- **Limitations**:
  - Distance is measured “as the crow flies,” not along road networks; actual travel distance may be longer.
  - Population data are from the 2010 Census, any shifts over the past decade are not captured.
  - The store directory may miss small or independent grocers that are not SNAP‑authorized or listed in TDLinx.
  - Tracts with large group‑quarters populations such as prisons can appear to have very poor food access, though the resident population may have on‑site food services. However, there is a flag to filter these out.

---

### Ethical and Legal Constraints

**Privacy**  
All data are aggregated to the census‑tract level. There are no individual or household‑level records included. The dataset is classified as **public access** and is licensed under **Creative Commons CCZero (CC0)**, placing it in the public domain. 

**Responsible Use**  
- The phrase “food desert” is no longer used by USDA‑ERS. The Atlas now uses “low‑income and low‑access” (LILA) terminology. 
- The binary LILA flags can oversimplify problems. A tract that misses the threshold by a single percentage point is not meaningfully different from one just above it.
- Since the data relies on 2010 census and 2014‑2018 income estimates, findings are more relevant for the early‑to‑mid 2010s period.

**Attribution**  
Economic Research Service (ERS), U.S. Department of Agriculture (USDA). Food Access Research Atlas. https://www.ers.usda.gov/data-products/food-access-research-atlas/.

---

### Dataset Relation to Research Questions

**Rural vs. Urban**

The Atlas’s `Urban`/`Rural` field allows for comparison of food‑access indicators of the rural and urban tracts. The hypothesis that **rural families face higher rates of food insecurity** can be tested by examining:

- The prevalence of LILA tracts in rural vs. urban areas, using any of the four distance measures.
- The continuous variables such as `LALowIncome_halfShare`, `LALowIncome_1Share` to see whether low‑income individuals in rural tracts are more likely to live far from a supermarket than urban counterparts.

**Identifying the highest‑burden counties and contributing factors**

- **Identifying counties**: By aggregating FARA tract flags to the county level, counties can be ranked by the share of residents living in LILA tracts. 
- **Co‑factors**: FARA includes several variables that can serve as  co‑factors: poverty rate, median family income, vehicle availability, and group‑quarters.
- **Suggestions**: The vehicle‑availability variables could useful to provide suggestions. If a rural county has high food insecurity, high LILA percentages, and a high share of zero‑vehicle households, a policy recommendation might combine public transit and grocery‑store investment. Another suggestion could be that if poverty rate is the dominant co‑factor, income‑support programs may be an effective policy. 

# Data quality: 

## Food Atlas (FARA) Data Quailty Assesment

### Accuracy
The dataset appears to be accurate. The FARA (Food Access Research Atlas) dataset was checked for negative values, and none appear in the dataset, which is an indicator of accurate data of this nature (counts, percentages and flags).

### Completeness
There are a significant amount of missing values (in this case, NaN values) in this dataset. The columns contain the bulk of the missing data, and there are no rows with all missing data. Some columns have over 41% missing values, such as LAPOP1_10 “Population count beyond 1 mile for urban areas or 10 miles for rural areas from supermarket”, which has 29957 missing values. To visualize this missing data, there are a few maps that show what counties are missing a specific column. Columns with a missing data overwhelming are columns that are using supermarket data, which makes sense. Presumably, the supermarket data may have been incomplete for more areas. 

### Timeliness
The Food Access Research Atlas is calculated based on census data from 2010 combined with other data from up to 2019. This data includes Urban or rural designation from 2019, data on income, vehicle availability, and SNAP participation from 2014-18 (American Community Survey), and lists of supermarkets, supercenters, and large grocery stores from 2019.
The population data is the most recent data available from the Food Access Research Atlas. Although food insecurity statistics are likely to have changed, as this data was before the 2020 COVID Pandemic, and it is now 2026, this data is the best available from an authoritative source. Also, counties, states, and FIPS codes will not change so all of those variables will still be accurate.  

Economic Research Service (ERS), U.S. Department of Agriculture (USDA). Food Access Research Atlas, https://www.ers.usda.gov/data-products/food-access-research-atlas/

### Consistency
The data appears to be consistent. The low-access population does not exceed total population, percentages are within [0,100], the values in the urban/rural flag columns were only 0 and 1, and there are no duplicate values in the CensusTract column. 

# Data cleaning: 

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


# Findings: 

# Future work:

## Mapping Alaska, Hawaii, and US Territories
We were only able to include the contiguous United States in our maps because of a lack of space and familiarity with the geopandas software. However, these two states are greatly affected by food insecurity as they have to import a lot of their food. Alaska is a fairly rural state which has a lot of low access areas. We are also missing data about the US Territories, such as Puerto Rico, which also face a similar issue. Because of the Jones Act of 1920 all goods imported to Puerto Rico must come from the US, which adds additional costs. It would be interesting to specifically explore these parts of the US which were not present in our analysis but which face additional challenges. 

## Modeling 
We only used a simple linear regression model to examine the relationship between food insecurity and population in each county as well as the urban/rural designation. This model helped us understand which variable had a stronger relationship, but both models had poor predictive power. In the future, we could add more features to try to predict this percentage. It is likely that poverty rate and cost per meal also have an impact on our response variable. We could also try using a beta regression model which will take into account the bounds on our response variable (a percentage between 0 and 1). 

## Interactive Visualizations
Feeding America has an interactive visualization for their Map the Meal Gap Data, which allows users to filter the data by race and age, as well as view data at the state and county levels. Hovering over a section of the map also brings up additional information. We could also create interactive visualizations using the altair library in python. For example, hovering over a state could show the specific value associated with it so viewers don’t just have to rely on the color scale. 


# Challenges: 

# Reproducing: 

### Python version
The project was created and tested on Python 3.12.3. 

### Python packages**

All required packages are listed in [requirements.txt](requirements.txt). Install them:

```bash
pip install -r requirements.txt
```

____


### Internet Access Dependency

-`geo_NaN_visuals.ipynb` and `geo_visuals.ipynb` download U.S. county and state shapefiles directly from the Census Bureau. These requests go to `https://www2.census.gov/geo/tiger/GENZ2019/shp/`.

---

### Data access

1. Food Access Research Atlas (FARA) — public

 `data/Food Access Research Atlas.csv`

Download from the USDA Economic Research Service:
> https://www.ers.usda.gov/data-products/food-access-research-atlas/

Place the downloaded CSV at:
```
data/Food Access Research Atlas.csv
```

 2. Map the Meal Gap (MMG) — restricted

 `data/MMG2025_2019-2023_Data_To_Share.xlsx`

This file is not publicly available. It must be requested from Feeding America, we requested the data for use in the course and were sent it over email.  
IS477 course staff: the file is available in the shared Box folder — download it and place it at:
```
data/MMG2025_2019-2023_Data_To_Share.xlsx
```
---

### How to run

From the project root directory:

```bash
python run_all.py
```

# References: 
