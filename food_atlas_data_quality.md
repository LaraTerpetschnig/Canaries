# Food Atlas (FARA) Data Profile
## Structure

The Food Access Research Atlas is avalible as a single Microsoft Excel file (`.xlsx`), with the 2019 edition weighing approximately 81.8 MB. Each row corresponds to a single U.S. Census tract, identified by a FIPS code. The 2010 Census tract geography serves is the spatial base for the data, so that when used in GIS (such as python's Geopandas and shapefiles), the spreadsheet must be joined to a 2010 tract boundary file. The columns contain attributes that can be grouped into catagories:

- **Identifiers & geography** – tract ID, state, county, and urban/rural status.
- **Demographics** – total population, number of housing units, poverty rate, median family income, low-income tract flag.
- **Food-access distance measures** – multiple binary flags and population counts that indicate whether the tract qualifies as low-income *and* low-access (formerly, “food deserts”) at combinations of ½‑mile, 1‑mile, 10‑mile, and 20‑mile thresholds, plus a vehicle‑access‑adjusted measure.
- **Sub‑population access indicators** – examples: number/percentage of children, seniors, low‑income individuals, and households without a vehicle who live far from a supermarket.

The `.zip` foler also includes a **data dictionary** sheet that defines every variable. Previous versions (2015, 2010) and the archived “Food Desert Locator” (2006) are also available as `.zip` downloads.

---
## Content 
### Demographic and Economic Variables

| Variable | Definition | Source |
|----------|------------|--------|
| `Pop2010` | Total number of persons residing in the tract (2010 U.S. Census). | 2010 U.S. Census block level data |
| `Housing2010` | Total housing units in the tract. | 2010 U.S. Census block level data |
| `PovertyRate` | Share of tract population with income ≤ federal poverty thresholds. | 2014‑2018 American Community Survey (ACS) 5‑year estimates |
| `MedianFamilyIncome` | Median family income of the tract (including families with zero income). | 2014‑2018 ACS |
| `LowIncomeTracts` | Binary flag (1/0) indicating whether the tract meets the NMTC low‑income definition (poverty ≥20 % OR median family income ≤80 % of state/metro median). | Department of Treasury’s New Markets Tax Credit (NMTC) program |
| `Urban` / `Rural` | Status based on the population‑weighted centroid. Urban if >2,500 people or otherwise rural. | Bureau of the Census urbanized area definitions |

### Food‑access Distance Measures

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

## Characteristics

- **Geography**: A Census tract isthe smallest level that consistent food‑access indicators are publicly available. This allows intra‑county analysis. However, the other dataset used in this project does not includedata for any area smaller than a county, so it will not be used in this project.
- **Timeliness**: The current version uses 2019 store data, 2010 Census populations, and 2014‑2018 ACS income data. The Atlas is updated periodically. 
- **Urban/rural**: Urban/rural status is assigned based on the tract’s population‑weighted centroid using the Census Bureau’s urbanized‑area definition (<2,500 = rural). Because distance thresholds differ for urban vs. rural tracts, the Atlas accounts for rural residents having to travel farther to reach a supermarket.
- **Limitations**:
  - Distance is measured “as the crow flies,” not along road networks; actual travel distance may be longer.
  - Population data are from the 2010 Census, any shifts over the past decade are not captured.
  - The store directory may miss small or independent grocers that are not SNAP‑authorized or listed in TDLinx.
  - Tracts with large group‑quarters populations such as prisons can appear to have very poor food access, though the resident population may have on‑site food services. However, there is a flag to filter these out.

---

## Ethical and Legal Constraints

**Privacy**  
All data are aggregated to the census‑tract level. There are no individual or household‑level records included. The dataset is classified as **public access** and is licensed under **Creative Commons CCZero (CC0)**, placing it in the public domain. 

**Responsible Use**  
- The phrase “food desert” is no longer used by USDA‑ERS. The Atlas now uses “low‑income and low‑access” (LILA) terminology. 
- The binary LILA flags can oversimplify problems. A tract that misses the threshold by a single percentage point is not meaningfully different from one just above it.
- Since the data relies on 2010 census and 2014‑2018 income estimates, findings are more relevant for the early‑to‑mid 2010s period.

**Attribution**  
Economic Research Service (ERS), U.S. Department of Agriculture (USDA). Food Access Research Atlas. https://www.ers.usda.gov/data-products/food-access-research-atlas/.

---

## Dataset Relation to Research Questions

**Rural vs. Urban**

The Atlas’s `Urban`/`Rural` field allows for comparison of food‑access indicators of the rural and urban tracts. The hypothesis that **rural families face higher rates of food insecurity** can be tested by examining:

- The prevalence of LILA tracts in rural vs. urban areas, using any of the four distance measures.
- The continuous variables such as `LALowIncome_halfShare`, `LALowIncome_1Share` to see whether low‑income individuals in rural tracts are more likely to live far from a supermarket than urban counterparts.

**Identifying the highest‑burden counties and contributing factors**

- **Identifying counties**: By aggregating FARA tract flags to the county level, counties can be ranked by the share of residents living in LILA tracts. 
- **Co‑factors**: FARA includes several variables that can serve as  co‑factors: poverty rate, median family income, vehicle availability, and group‑quarters.
- **Suggestions**: The vehicle‑availability variables could useful to provide suggestions. If a rural county has high food insecurity, high LILA percentages, and a high share of zero‑vehicle households, a policy recommendation might combine public transit and grocery‑store investment. Another suggestion could be that if poverty rate is the dominant co‑factor, income‑support programs may be an effective policy. 