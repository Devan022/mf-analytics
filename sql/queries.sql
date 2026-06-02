-- 1 Top 5 funds by NAV
SELECT * FROM nav_history
ORDER BY nav DESC
LIMIT 5;

-- 2 Total schemes
SELECT COUNT(*) FROM fund_master;

-- 3 Average NAV
SELECT AVG(nav) FROM nav_history;

-- 4 Highest NAV
SELECT MAX(nav) FROM nav_history;

-- 5 Lowest NAV
SELECT MIN(nav) FROM nav_history;

-- 6 NAV count by source file
SELECT source_file, COUNT(*)
FROM nav_history
GROUP BY source_file;

-- 7 Latest NAV date
SELECT MAX(date)
FROM nav_history;

-- 8 Total records in fund master
SELECT COUNT(*)
FROM fund_master;

-- 9 Total records in NAV history
SELECT COUNT(*)
FROM nav_history;

-- 10 Average NAV by source file
SELECT source_file,
AVG(nav)
FROM nav_history
GROUP BY source_file;