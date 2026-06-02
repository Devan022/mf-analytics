import pandas as pd
import os

files = [
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv"
]

for f in files:
    df = pd.read_csv(f"data/raw/{f}")
    print("\n", f)
    print(df.columns.tolist())