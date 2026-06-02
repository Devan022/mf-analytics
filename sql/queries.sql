-- 1. Top 5 Fund Houses by AUM
SELECT fund_house,
       SUM(aum_crore) AS total_aum
FROM aum_data
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- 2. Average Monthly SIP Inflow
SELECT AVG(sip_inflow_crore) AS avg_monthly_sip
FROM sip_data;

-- 3. SIP YoY Growth Trend
SELECT month,
       yoy_growth_pct
FROM sip_data
ORDER BY month;

-- 4. Transactions by State
SELECT state,
       COUNT(*) AS transaction_count
FROM investor_transactions
GROUP BY state
ORDER BY transaction_count DESC;

-- 5. Funds with Expense Ratio < 1%
SELECT scheme_name,
       fund_house,
       expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- 6. Top 10 Funds by 5-Year Return
SELECT scheme_name,
       return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 7. Highest Sharpe Ratio Funds
SELECT scheme_name,
       sharpe_ratio
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- 8. Average Investment Amount by State
SELECT state,
       ROUND(AVG(amount_inr),2) AS avg_investment
FROM investor_transactions
GROUP BY state
ORDER BY avg_investment DESC;

-- 9. Transactions by Payment Mode
SELECT payment_mode,
       COUNT(*) AS transaction_count
FROM investor_transactions
GROUP BY payment_mode
ORDER BY transaction_count DESC;

-- 10. Fund Houses with Maximum Number of Schemes
SELECT fund_house,
       SUM(num_schemes) AS total_schemes
FROM aum_data
GROUP BY fund_house
ORDER BY total_schemes DESC
LIMIT 10;