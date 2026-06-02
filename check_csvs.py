import pandas as pd
import os

for file in os.listdir("data/raw"):
    if file.endswith(".csv"):
        try:
            df = pd.read_csv(f"data/raw/{file}")
            print(f"✅ {file}: {df.shape}")
        except Exception as e:
            print(f"❌ {file}")
            print(e)
            print("-" * 50)