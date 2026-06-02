import pandas as pd
import os
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

for file in os.listdir("data/processed"):

    if file.endswith(".csv"):

        table = file.replace(".csv","")

        df = pd.read_csv(
            f"data/processed/{file}"
        )

        df.to_sql(
            table,
            engine,
            if_exists="replace",
            index=False
        )

        print("Loaded", table)

print("Database Created")