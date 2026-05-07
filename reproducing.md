# Reproducing the Analysis

### Python version
The project was created and tested on Python 3.12.3. 

### Python packages

All required packages are listed in [requirements.txt](requirements.txt). Install them:

```bash
pip install -r requirements.txt
```

____


### Internet Access Dependency

-`geo_NaN_visuals.ipynb` and `geo_visuals.ipynb` download U.S. county and state shapefiles directly from the Census Bureau. These requests go to `https://www2.census.gov/geo/tiger/GENZ2019/shp/`.

---

## Data access

### 1. Food Access Research Atlas (FARA) — public

 `data/Food Access Research Atlas.csv`

Download from the USDA Economic Research Service:
> https://www.ers.usda.gov/data-products/food-access-research-atlas/

Place the downloaded CSV at:
```
data/Food Access Research Atlas.csv
```

### 2. Map the Meal Gap (MMG) — restricted

 `data/MMG2025_2019-2023_Data_To_Share.xlsx`

This file is not publicly available. It must be requested from Feeding America, we requested the data for use in the course and were sent it over email.  
IS477 course staff: the file is available in the shared Box folder — download it and place it at:
```
data/MMG2025_2019-2023_Data_To_Share.xlsx
```
---

## How to run

From the project root directory:

```bash
python run_all.py
```