import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

files = {
    "01_fund_master.csv": "https://drive.google.com/file/d/1vxvhJB2gVKsLfv51pXcLa39hnOr7M6vZ/view?usp=sharing",
    "02_nav_history.csv": "https://drive.google.com/file/d/10GfFYNtj-yqUoJ05zxkFhti0DkEW_CuZ/view?usp=sharing",
    "03_aum_by_fund_house.csv": "https://drive.google.com/file/d/1SY1wVj6aU3coZcPVE5DuWxUOj5mtUP4T/view?usp=sharing",
    "04_monthly_sip_inflows.csv": "https://drive.google.com/file/d/1NoQEbNNZyenLShtBM4CRjrh6c5lhx5Qy/view?usp=sharing",
    "05_category_inflows.csv": "https://drive.google.com/file/d/1M-OqSJBEz-so0Q69PzMZBq10ON_WaI17/view?usp=sharing",
    "06_industry_folio_count.csv": "https://drive.google.com/file/d/1rgkdnDbv0GcjZgfdczqr7kkVB7cGBz4s/view?usp=sharing",
    "07_scheme_performance.csv": "https://drive.google.com/file/d/1N65c5EcrgYQmDJUAs8cxyZnp9WV10izk/view?usp=sharing",
    "08_investor_transactions.csv": "https://drive.google.com/file/d/1zRk1hIJ1gF2vmmYbXFuKmpaFDzTiFIFj/view?usp=sharing",
    "09_portfolio_holdings.csv": "https://drive.google.com/file/d/1O2cXuQhc8SMOcYY38fCJF7IErOqaP6iv/view?usp=sharing",
    "10_benchmark_indices.csv": "https://drive.google.com/file/d/13VZkUoJlyXADh3M9kbaXLi9cVEJs_76s/view?usp=sharing"
}

for filename, url in files.items():
    print(f"Downloading {filename}...")

    df = pd.read_csv(url)

    df.to_csv(
        f"data/raw/{filename}",
        index=False
    )

    print(f"Saved {filename}")

print("\nAll datasets downloaded successfully!")