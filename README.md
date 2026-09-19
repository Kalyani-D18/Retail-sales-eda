# Retail Sales - Exploratory Data Analysis

Data Science/ Data Analytics project: clean a messy
retail sales export and explore it with Python and Pandas, producing
basic statistics and visualizations.

## Why this project

project by covering the Python-for-data side specifically: Pandas-based
cleaning, exploratory data analysis, and basic statistics — the core
skills behind most fresher Data Analyst / Data Engineer screening tests.

## Tech stack

Python - Pandas - NumPy - Matplotlib - Seaborn - Jupyter Notebook

## Project structure

```
retail-sales-eda/
── sales_raw.csv          # generated messy dataset
├── images/                        # charts exported from the notebook
├── generate_sales_data.py         # generates the sample raw dataset
├── Retail_Sales_EDA.ipynb         # the analysis notebook
└── requirements.txt
```

## What the notebook covers

1. **Load & inspect** the raw CSV (`shape`, `dtypes`, `head`, `info`)
2. **Data quality check** — missing values per column, duplicate rows
3. **Data cleaning**
   - drop exact duplicates
   - standardize inconsistent text casing (`WEST` / `west` / `West`)
   - convert and coerce numeric columns
   - impute missing `sales` using the **category median** (not a blind
     global fill), missing `quantity`/`profit` with the column median,
     missing `region` as `"Unknown"`
4. **Descriptive statistics** — `describe()` on the numeric columns
5. **Exploratory analysis**
   - total sales by category (bar chart)
   - total profit by region (bar chart)
   - sales share by customer segment (pie chart)
   - monthly sales trend (line chart)
   - correlation matrix between quantity, sales, discount, and profit (heatmap)
6. **Key insights** — a short written summary of what the data shows
7. **Possible next steps** — loading into MySQL, a basic regression model,
   a Power BI dashboard

## Setup

```bash
pip install -r requirements.txt

# 1. Generate the raw sample dataset
python generate_sales_data.py

# 2. Open the notebook
jupyter notebook Retail_Sales_EDA.ipynb
```

Run all cells top to bottom. Because the raw data is generated with a
fixed random seed, re-running the notebook reproduces the same numbers
described in the "Key insights" section.

## Notes

- `data/raw/sales_raw.csv` is synthetic data generated locally by
  `generate_sales_data.py` — not real sales data.
- `images/` contains chart exports from a full run of the notebook, so
  the results are visible on GitHub without needing to run Jupyter.
