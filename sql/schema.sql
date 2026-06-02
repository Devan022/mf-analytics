CREATE TABLE dim_fund (
    scheme_code INTEGER PRIMARY KEY,
    scheme_name TEXT
);

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    date TEXT
);

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER,
    date TEXT,
    nav REAL
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT
);