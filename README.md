# Urban & Rural Divides in U.S. Food Insecurity

## Contributors:

- Lily Rybka
-  Lara Terpetschnig 

(Team: Canaries)

# Summary
## Motivation
We have a history of volunteering at food pantries and food banks in the local community. We are both connected to the University YMCA which hosts community meals through UniPlace Church and Interfaith in Action, which Lily is a member of. Lara is a member of another Y-affiliated organization, Project4Less, which is a food recovery club. We wanted to learn more about food insecurity on a larger scale and we felt that our experiences working with these organizations would help inform our approach to the data. We had previously visited the Feeding America website to look at the food insecurity rate for Champaign County, which is how we found the Map the Meal Gap dataset. 
## Description
In this project, we clean and combine two datasets related to food access and food insecurity to get a more holistic view of the barriers that exist in America. Our county-level dataset is then visualized to show how different indicators of need overlap. We used a linear regression model to compare the impact of rural and urban designations and population on food insecurity. All our results are carefully documented to be fully reproducible.  
## Research Questions
* Do families living in rural areas have higher rates of food insecurity compared to families living in urban areas?
  * Does the overall trend hold up when looking at the data state-by-state?
  * Is population count (per county) a better or worse indicator of food insecurity compared to urban and rural designations?
* How does food access (measured by the Food Access Research Atlas) and food insecurity (measured by Map the Meal Gap) overlap?
  * Do each of these datasets identify similar geographic areas of concern?
  * How can these two datasets be combined to create a more holistic view of food insecurity?
* Which counties in the US suffer from the highest rates of food insecurity?
  * What cofactors are contributing to the situation?
  * What suggestions could be made to improve the situation?
## Findings
Each dataset has valuable information that we were able to compare when they were combined. Food access and food insecurity have some overlap but access does not account for all cases of food insecurity. We found that counties that are designated as rural have a high rate of food insecurity compared to counties designated as urban. Furthermore, the Rural Urban Continuum Code is a better indicator of food insecurity compared to population per county. Finally, counties in Southern states tend to have the worst rates of food insecurity, with Mississippi having the highest average food insecurity rate out of the 50 states. 

## Project Tree
Canaries/
│
├── README.md                          
│
├── data/                              
│   ├── Food Access Research Atlas.csv 
│   ├── Meal_Gap_2019.csv              
│   ├── MMG_FARA_2019_county.csv  
│
├── hash digest/                    
│   ├── fara.sha                      
│   └── mmg.sha                        
│
├── notebooks/                          
│   ├── data_integrity.ipynb              
│   ├── food_atlas_data_quality.ipynb  
│   ├── meal_gap_data_quality.ipynb    
│   ├── data_merge_fips.ipynb   
│   ├── bar_graph.ipynb             
│   ├── geo_visuals.ipynb    
│   ├── geo_NaN_visuals.ipynb        
│   └── linear_regression_model.ipynb 
└── visualizations/                
    ├── High/Low_Food_Insecurity_Rates.png
    ├── urban_rural_food_insecurity.png
    ├── urban_rural_pct_black/kids/latine/white_food_insecure.png
    ├── urban_rural_poverty_rate.png
    ├── urban_rural_weekly_food_budget.png
    ├── mmg_fara_test_maps.png
    └── missing_*_data_map.png  (* maps of missingness by variable)

# Data profile 

## Food Access Research Atlas (FARA)

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

## Map the Meal Gap (MMG)
### Location
The original file is located in [this Box folder](https://uofi.box.com/s/73j874awu6svsiwn25d8s6nbc5frxmqw) because the data is not publicly available. 
### Structure
The data was shared with us in an excel file that contained all Map the Meal Gap data from 2019 to 2023. This file contains six sheets. The two we used are ‘Read Me’ which is a data dictionary and `County` which contains the county level data. The other spreadsheets contain data aggregated by different units, like state and congressional district, which were not useful for our analysis. The size of the spreadsheet is 2.5MB. 

Each row corresponds to a county. The column attributes can be grouped as follows:
- **identifiers and geography** - FIPS, state code, and county name
- **percent and number of food insecure** - total and breakdown for race (White, Black, Latine) and age (children) 
- **SNAP** - related to the Supplemental Nutrition Access Program, which many food insecure people are a part of 
- **cost and budget** - amount of money needed to purchase meals and current budget deficit 

### Content
The following columns are relevant to our analysis after data cleaning. Note that during the cleaning process, all of the column names were changed to better reflect the combined dataset. 
| Column Name                                  | Description                                                                                                                                              |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| FIPS                                         | Federal Information Processing Standards code for each county                                                                                            |
| State                                        | Two letter state code                                                                                                                                    |
| County                                       | County name                                                                                                                                              |
| pctFoodInsecure, numFoodInsecure             | Percent/number of people who are food insecure                                                                                                           |
| pctBlackFoodInsecure                         | Percent of Black people who are food insecure                                                                                                            |
| pctLatineFoodInsecure                        | Percent of Latine people who are food insecure                                                                                                           |
| pctWhiteFoodInsecure                         | Percent of White people who are food insecure                                                                                                            |
| pctFIbelowSNAP, pctFIaboveSNAP               | Percent of food insecure people whose income is above and below the threshold for SNAP                                                                   |
| pctKidsFoodInsecure, numKidsFoodInsecure     | Percent/number of kids who are food insecure                                                                                                             |
| pctKidsIncomeBelow185, pctKidsIncomeAbove185 | Percent of food insecure kids who live above and below 185% of the federal poverty line, which is the cutoff for many food assistance programs for kids  |
| costPerMeal                                  | Average amount spent per meal                                                                                                                            |
| weeklyFoodBudget                             | Amount of money needed per week for food insecure person to pay for food                                                                                 |
| weeklyBudgetFoodInsecureByPop                | weeklyFoodBudget multiplied by population                                                                                                                |
| rangeRuralUrban                              | Rural-Urban Continuum Code, ranges from 1 to 9                                                                                                           |

### Constraints 
#### Ethical
All of the data is aggregated at the county level, there is no risk of tracing the data back to an individual. 
#### Legal
The Map the Meal Gap data is not publicly available. We requested the data through a form on the Feeding America website. In order to not publicize the data, we have uploaded it to a Box folder that requires U of I credentials to access it. We were requested to read the documentation for the data to ensure that we used it responsibly and to share any report we produced with them. We were not able to find a license for the data in any of the documentation. 
### Relation to Research Questions
The data contains a column with the Rural Urban Continuum Code, which ranges from 1 to 9 and is based on the population in each county and whether or not the county is adjacent to a metro area. Codes 1 to 3 represent metro counties and codes 4 to 9 represent nonmetro counties. We can use this column to measure how rural or urban the county is, or create a binary flag based on a threshold.   

It also contains county-level data which, when combined with the Food Access Research Atlas can give a more holistic view of food insecurity. Food access is one part of being food insecure, but does not necessarily take into account the budget of each person or the type of food store they are near. We can also pinpoint which counties have the highest rates of food insecurity and use the combined datasets to identify which factors may be causing this. 



# Data quality 

## Food Atlas Research Atlas (FARA)

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

## Map the Meal Gap (MMG)
### Accuracy
The documentation notes that the food insecurity percentages for each county are estimates based off of data from the Current Population Survey from the Bureau of Labor Statistics. The estimates produced from their models may not reflect the actual percentage of food insecurity because they are dependent on the available data. For example, there is no data about underemployment (when people are employed but not making enough money), so this variable cannot be included. However, underemployed people are likely being estimated as food insecure. 
We checked the dataset to ensure that all of the state codes were correct and that the urban/rural designation for each county is between 1 and 9. 
### Completeness 
There are many missing values for food insecurity rates broken down by race (find actual number). This is because there was not always enough publicly available data for Feeding America to create reliable estimates. In addition, they did not include counts for each race, only the percentage, as the small sample sizes created large confidence intervals. The documentation recommends combining the estimates from the map with local data and conversations with people facing food insecurity in the county, as providing numbers could be misleading. 
Refer to the maps below to see which counties have data for food insecurity for each race. We observe that estimates for Black people are present mostly in the South, while estimates for Latine people are present except for parts of the Midwest and New England. There are only a few counties missing estimates for White people. 
There are no missing values in any of the other columns. 
### Timeliness
Feeding America updates Map the Meal Gap every year; however, we chose to use the data from 2019 because that matches the timeliness of the other dataset. (The Food Access Research Atlas is calculated based on data from 2019.) The food insecurity estimates are likely to change every year while the county and state names, as well as the corresponding FIPS code, remain the same throughout and can be used for combining datasets and for comparison between years. This data is suitable for our needs because it is fairly recent and still provides a good estimate of food insecurity in 2026. 
### Consistency
- We checked to ensure that the percentage values were in between 0 and 100.
- We checked that each of the FIPS codes are unique because they should each correspond to a different county. 
- We checked that the combination of state code and county is unique. Some counties may have the same name in different states (for example, Urbana, IL and Urbana, IN) so this county name alone is not a unique identifier. 


# Data cleaning 

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


# Findings
**Research Question #1: Do families living in rural areas have higher rates of food insecurity compared to families living in urban areas?** 

We created two maps to show the difference in food insecurity rates in both the rural and urban areas at both the state level and the county level. 

For the state level, we aggregate the data by taking the mean of the food insecurity rate for all rural and urban counties in each state. Then we calculated the difference between the two averages, which are plotted on the left. The state is a shade of red if the rural average is higher and a shade of blue if the urban average is higher. We can see that most states have a higher food insecurity rate among rural counties, with the exception of North Dakota and a couple states in New England. The county level data is plotted directly, with rural counties represented with red and urban counties represented with blue. We can see that there are more urban tracts with high rates of food insecurity (around 20%). 
![map](https://github.com/LaraTerpetschnig/Canaries/blob/main/visualizations/urban_rural_food_insecurity.png)

We also filtered the data by race to create the same maps for Black, Latine, and White individuals. Because of a lack of data for Black and Latine populations, some states are grey to indicate that we were not able to calculate an average for that state. 
![map_white](https://github.com/LaraTerpetschnig/Canaries/blob/main/visualizations/urban_rural_pct_white_food_insecure.png)
![map_black](https://github.com/LaraTerpetschnig/Canaries/blob/main/visualizations/urban_rural_pct_black_food_insecure.png)
![map_latine](https://github.com/LaraTerpetschnig/Canaries/blob/main/visualizations/urban_rural_pct_latine_food_insecure.png)
 
**Research Question #2: How does food access (measured by the Food Access Research Atlas) and food insecurity (measured by Map the Meal Gap) overlap?** 

By combining the two datasets, we were able to see the impact of poverty on food insecurity. As we expected, there is a high overlap between counties with a high food insecurity rate (over 20% and a high poverty rate (over 30%). 

In addition, we were able to compare counties designated as low income and low access by the Food Access Research Atlas with the food insecurity rate. There was some overlap between these designations in Utah and the Dakotas however, parts of Mississippi and Arkansas were designated as fairly high income and access while still having a high food insecurity rate. This could be because there are other factors that contribute to food insecurity and we may have lost some granularity by averaging the Food Access Research Atlas data for each county, as it was originally by census tract. 

![map_compare](https://github.com/LaraTerpetschnig/Canaries/blob/main/visualizations/mmg_fara_test_maps.png)

**Research Questions #3: Which counties in the US suffer from the highest rates of food insecurity?**

We made a bar graph of the counties with the highest food insecurity rates in the nation. Most of these counties were in the South (Mississippi, Arkansas, Kentucky). The county with the highest rate of food insecurity is Issaquena County, which has a population that is 62.2% Black. Systematic racism and redlining still have an impact today which can be seen through the location of food stores, which contribute to food insecurity. In general, states in the South have a higher food insecurity rate. The top five most food insecure states are all in the South. 
Three of the counties were in South Dakota, with the highest in the state being Oglala Lakota County, which is part of a Lakota reservation. This highlights how Native American reservations are especially vulnerable, likely due to historical factors like being driven out of their ancestral land and systematic racism. 
Future federal programs could use this data to target counties within reservations with additional resources. 

![bar_graph](https://github.com/LaraTerpetschnig/Canaries/blob/main/visualizations/Average_Food_Insecurity_Rate_State.png)

For addition visualization, check the `visualizations` folder. 

## Modeling 
### Is Population Count a Better Predictor of Food Insecurity Than Urban/Rural Classification?

We can see a distribution of the number of states within each code (1 through 9) below.

At the U.S. county level, does 2010 Census population (`Pop2010`) or urban/rural status (`Urban`) better predict the share of the population that is food insecure (`pctFoodInsecure`)?

To answer our research question, we ran an OLS linear regression with `pctFoodInsecure ~ log₁₀(Pop2010) + Urban_prop`.
**A: Urban/rural classification is the stronger predictor than county population count**


### OLS Results: `pctFoodInsecure ~ log₁₀(Pop2010) + Urban_prop`


| Predictor | Coefficient | Standardized β | p-value |
|---|---|---|---|
| log₁₀(Pop2010) | −0.0009 | ~−0.024 | 0.577 — not significant |
| Urban_prop | −0.0224 | ~−0.160 | < 0.001 — significant |

We can see that the rural-urban designation is a better predictor, but only slightly. They are both very weak.


# Future work

## Mapping Alaska, Hawaii, and US Territories
We were only able to include the contiguous United States in our maps because of a lack of space and familiarity with the geopandas software. However, these two states are greatly affected by food insecurity as they have to import a lot of their food. Alaska is a fairly rural state which has a lot of low access areas. We are also missing data about the US Territories, such as Puerto Rico, which also face a similar issue. Because of the Jones Act of 1920 all goods imported to Puerto Rico must come from the US, which adds additional costs. It would be interesting to specifically explore these parts of the US which were not present in our analysis but which face additional challenges. 

## Modeling 
We only used a simple linear regression model to examine the relationship between food insecurity and population in each county as well as the urban/rural designation. This model helped us understand which variable had a stronger relationship, but both models had poor predictive power. In the future, we could add more features to try to predict this percentage. It is likely that poverty rate and cost per meal also have an impact on our response variable. We could also try using a beta regression model which will take into account the bounds on our response variable (a percentage between 0 and 1). 

## Interactive Visualizations
Feeding America has an interactive visualization for their Map the Meal Gap Data, which allows users to filter the data by race and age, as well as view data at the state and county levels. Hovering over a section of the map also brings up additional information. We could also create interactive visualizations using the altair library in python. For example, hovering over a state could show the specific value associated with it so viewers don’t just have to rely on the color scale. 


# Challenges 
## Merging the data
We originally merged the datasets together before our second checkpoint on a combination of the county name and state. In the process, we dropped the FIPS code, which we thought was irrelevant. We later learned that FIPS (Federal Information Processing Standard) is a standardized five number code that uniquely identifies each county, and it is helpful for visualizing data with mapping software like geopandas. For example, the FIPS code for Champaign County is 17019. We merged the data a second time on the FIPS code. This was also necessary to combine the official state and county borders with our data. 
## File Size
The Food Access Research Atlas dataset is about 45MB, so it is close to the limit for file size in Github, which is 50MB. When we first tried to upload the dataset, we got an error saying that it was too large to push. We decided to separate the dataset into three “chunks” which were about 15MB each. We then combined them into one dataframe which was stored locally. However, we were later able to successfully push the original dataset to Github and deleted those files. We are unsure what originally caused the error as the dataset was not technically outside of the limits. 
## Large Feature Size
Both of our datasets had a large number of columns. The Food Access Research Atlas dataset originally had 147 columns, many of which were named in a way that confused us (ex. PCTGQTRS). The Map the Meal Gap dataset had 24 columns, which were in an excel spreadsheet that had long names for each column (ex. % food insecure children in HH w/ HH incomes below 185 FPL). In order to make the large volume of data easier to understand, we went through each column and looked at the documentation to understand what it meant so we could rename it. This took a couple hours but it helped us figure out which columns we wanted to focus on for our analysis. Although our naming schema may still be confusing, we think it is more human-readable while still being concise enough to be used for data analysis. 
## Large Amount of Missing Data
Both datasets contain breakdowns for race and ethnicity. The Food Access Research Atlas contains categories for White, Black, Asian, Native Hawaiian or Other Pacific Islander, American Indian or Alaska Native, and Other/multiple race as well as Hispanic or Latino. These categories are from the 2010 census. Map the Meal Gap contains data about Black, Latine, and White individuals. There is a lot of missing data for any race that is not White. We considered dropping these rows, but this would remove rows that have useful information in other columns. Instead, we decided to highlight these missing values in our visualizations to show that there may be counties with high food insecurity rates for minorities that we have not identified. There are also minority groups that are not represented in the data as Map the Meal Gap has only three categories for race. Despite this, we know that American Indian/Native American people face very high rates of food insecurity.


# Reproduction 

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
Dewey, A., Hilvers, J., Dawes, S., Harris, V., Hake, M., and Engelhard, E.
 (2025). Map the Meal Gap: A Report of Local Food Insecurity and Food Costs in the United
 States in 2023. Feeding America National Organization.
 https://www.feedingamerica.org/research/map-the-meal-gap/overall-executive-summary

Economic Research Service (ERS), U.S. Department of Agriculture (USDA). Food Access Research Atlas, https://www.ers.usda.gov/data-products/food-access-research-atlas/

geopandas/geopandas: Version 1.1.3 geopandas.org/

"U.S. Census Bureau. TIGER/Line Shapefiles. [2026]. Available at: https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html."

