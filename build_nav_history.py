import pandas as pd
import os

folder = "data/raw"

dfs = []

for file in os.listdir(folder):

    if file.endswith(".csv") and file != "fund_master.csv":

        df = pd.read_csv(
            os.path.join(folder, file)
        )

        df["source_file"] = file

        dfs.append(df)

nav_history = pd.concat(
    dfs,
    ignore_index=True
)

nav_history.to_csv(
    "data/raw/nav_history.csv",
    index=False
)

print("Shape:")
print(nav_history.shape)

print("Created nav_history.csv")