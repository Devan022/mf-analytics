import pandas as pd

fund_master = pd.read_csv(
    "data/raw/fund_master.csv"
)

nav_history = pd.read_csv(
    "data/raw/nav_history.csv"
)

print("Fund Master Shape:")
print(fund_master.shape)

print("\nNAV History Shape:")
print(nav_history.shape)

print("\nMissing Values:")
print(fund_master.isnull().sum())

print("\nDuplicate Rows:")
print(fund_master.duplicated().sum())