import requests
import pandas as pd

schemes = {
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for name, code in schemes.items():

    print(f"\nFetching {name}...")

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)
    data = response.json()

    print("Scheme:")
    print(data["meta"]["scheme_name"])

    df = pd.DataFrame(data["data"])

    filename = f"data/raw/{name}.csv"

    df.to_csv(
        filename,
        index=False
    )

    print(f"Saved: {filename}")