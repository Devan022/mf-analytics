import pandas as pd
import os

RAW = "data/raw"
PROCESSED = "data/processed"

os.makedirs(PROCESSED, exist_ok=True)

for file in os.listdir(RAW):
    if file.endswith(".csv"):

        path = os.path.join(RAW, file)

        try:
            df = pd.read_csv(path)

            df = df.drop_duplicates()

            for col in df.columns:
                if df[col].dtype == "object":
                    df[col] = df[col].astype(str).str.strip()

            out = os.path.join(PROCESSED, file)

            df.to_csv(out, index=False)

            print(f"Saved: {file}")

        except Exception as e:
            print(file, e)