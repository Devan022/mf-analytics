import pandas as pd

url = "https://www.amfiindia.com/spages/NAVAll.txt"

df = pd.read_csv(
    url,
    sep=";",
    engine="python",
    on_bad_lines="skip"
)

print(df.head())
print("\nColumns:")
print(df.columns)

df.to_csv(
    "data/raw/fund_master.csv",
    index=False
)

print("\nfund_master.csv created successfully")