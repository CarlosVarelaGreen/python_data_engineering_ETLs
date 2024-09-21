-- display only the entries with more than a 100 billion USD economy.
SELECT *
FROM 
    Countries_by_GDP
WHERE GDP_USD_billion > 100
ORDER BY GDP_USD_billion DESC;