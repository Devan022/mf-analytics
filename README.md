# Mutual Fund Analytics Capstone

## Project Overview

This project analyzes mutual fund performance, investor behavior, SIP trends, risk metrics, and market benchmarks using Python, SQLite, and Tableau.

The objective is to build an end-to-end analytics pipeline that performs:

- Data ingestion
- Data cleaning
- Exploratory data analysis
- Performance analytics
- Risk analytics
- Investor analytics
- Dashboard creation
- Fund recommendation system

---

## Project Architecture

Raw Data Sources
↓
Python ETL Pipeline
↓
Processed CSV Files
↓
SQLite Database
↓
Analytics Notebooks
↓
Tableau Dashboards
↓
Reports & Recommendations

---

## Data Sources

### MFAPI

Used for historical NAV data collection.

### AMFI

Used for mutual fund master information.

### Synthetic Investor Dataset

Contains:

- Investor transactions
- SIP investments
- Redemption records
- Geographic details
- Demographic information

---

## Folder Structure

```text
mf-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 03_eda_analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── reports/
│
├── dashboard/
│
├── recommender.py
│
└── README.md
```

## Technologies Used

- Python
- Pandas
- NumPy
- SQLite
- Matplotlib
- Tableau Public
- Jupyter Notebook

---

## Key Analyses Performed

### Exploratory Data Analysis

- Investor distribution by state
- Investor distribution by city tier
- Gender split analysis
- Age group analysis
- Monthly transaction trends

### Performance Analytics

- CAGR analysis
- Alpha/Beta analysis
- Sharpe ratio comparison
- Fund scorecard creation
- NAV trend analysis

### Advanced Analytics

- Value at Risk (VaR)
- Conditional Value at Risk (CVaR)
- Rolling 90-Day Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Fund Recommendation Engine

---

## Dashboard Components

### Dashboard 1

- SIP Trend
- Nifty 50 Trend
- Category Heatmap
- Top Categories

### Dashboard 2

- Transaction by State
- Transaction Type Split
- Age Group Analysis
- Monthly Volume

### Dashboard 3

- Fund Risk vs Return
- NAV Trend
- Fund Scorecard

### Dashboard 4

- AUM Trend
- AUM by AMC
- KPI Cards

---

## Recommendation Engine

Users can enter:

- Low
- Moderate
- High

Risk appetite.

The system recommends top-performing funds based on Sharpe Ratio and risk category.

Run:

```bash
python3 recommender.py
```

---

## How To Run

Activate environment:

```bash
source venv/bin/activate
```

Run notebooks in order:

1. 03_eda_analysis.ipynb
2. Performance_Analytics.ipynb
3. Advanced_Analytics.ipynb

Run recommender:

```bash
python3 recommender.py
```

---

## Key Findings

- Mid-cap funds generated highest risk-adjusted returns.
- SIP participation remained stable across investor groups.
- 2024 investor cohort contributed the highest investment volume.
- Liquid category recorded the highest net inflows.
- Risk and return showed positive correlation across major funds.

---

## Author

Devansh Tiwari

B.Tech Computer Science

MIT Manipal
