import pandas as pd
import os

folder = "data/raw"

files = [f for f in os.listdir(folder) if f.endswith(".csv")]

print(f"\nFound {len(files)} CSV files")

for file in files:

    print("\n" + "="*70)
    print(f"FILE: {file}")

    df = pd.read_csv(os.path.join(folder, file))

    print("\nSHAPE:")
    print(df.shape)

    print("\nDTYPES:")
    print(df.dtypes)

    print("\nHEAD:")
    print(df.head())

    print("\nMISSING VALUES:")
    print(df.isnull().sum())

    print("\nDUPLICATES:")
    print(df.duplicated().sum())