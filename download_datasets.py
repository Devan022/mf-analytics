import gdown
import os

os.makedirs("data/raw", exist_ok=True)

files = {
    "03_aum_by_fund_house.csv": "https://drive.google.com/file/d/1SY1wVj6aU3coZcPVE5DuWxUOj5mtUP4T/view",
    "04_monthly_sip_inflows.csv": "https://drive.google.com/file/d/1NoQEbNNZyenLShtBM4CRjrh6c5lhx5Qy/view",
    "05_category_inflows.csv": "https://drive.google.com/file/d/1M-OqSJBEz-s0Q069PzMZBq100N_WaI17/view",
    "06_industry_folio_count.csv": "https://drive.google.com/file/d/1rgkdnDbv0GcjZgfdczqr7kkVB7cGBz4s/view",
    "07_scheme_performance.csv": "https://drive.google.com/file/d/1N65c5EcrgYQmDJUAs8cxyZnp9WV10izk/view",
    "08_investor_transactions.csv": "https://drive.google.com/file/d/1zRk1hIJ1gF2vmmYbXFuKmpaFDzTiFlFj/view",
    "09_portfolio_holdings.csv": "https://drive.google.com/file/d/102cXuQhc8SMOcYY38fCJF7IErOqaP6iv/view",
    "10_benchmark_indices.csv": "https://drive.google.com/file/d/13VZkUoJlyXADh3M9kbaXLi9cVEJs_76s/view"
}

for filename, url in files.items():
    print(f"Downloading {filename}...")
    gdown.download(url, f"data/raw/{filename}", fuzzy=True)

print("\nAll datasets downloaded successfully!")