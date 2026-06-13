import pandas as pd
# Load scheme performance data
df = pd.read_csv("data/processed/07_scheme_performance.csv")
# User input
risk = input("Enter Risk Appetite (Low/Moderate/High): ").strip().capitalize()
# Filter funds by risk grade
filtered = df[df["risk_grade"] == risk]
# Check if any funds match
if filtered.empty:
    print(f"No funds found for risk grade: {risk}")
else:
    # Top 3 funds by Sharpe Ratio
    recommendations = filtered.sort_values(
        by="sharpe_ratio",
        ascending=False
    ).head(3)
    print("\nTop 3 Recommended Funds:\n")
    cols = [
        "scheme_name",
        "fund_house",
        "category",
        "sharpe_ratio",
        "return_3yr_pct",
        "risk_grade"
    ]
    print(recommendations[cols])
    # Save output
    recommendations[cols].to_csv(
        "recommended_funds.csv",
        index=False
    )
    print("\nRecommendations saved to recommended_funds.csv")