# Importing packages:
import pandas as pd
import os
import sqlalchemy

# Connecting to MySQL database:
host = os.environ.get('mysql_host')
user = os.environ.get('mysql_user')
password = os.environ.get('mysql_password')
engine = sqlalchemy.create_engine(f'mysql+pymysql://{user}:{password}@{host}/trading')


# Read table content:
pd.read_sql_query(
    """
    SELECT *
    FROM transactions
    LIMIT 10;
    """,
    engine
)

# What if we want the number of transactions per year for bitcoin and ethereum?


# Solution 1 - With the years on columns:
pd.read_sql_query(
    """
    SELECT
      ticker,
      COUNT(*) AS transactions_count,
      SUM(CASE WHEN EXTRACT(YEAR FROM txn_date)=2017 THEN 1 END) AS 2017_count,
      SUM(CASE WHEN EXTRACT(YEAR FROM txn_date)=2018 THEN 1 END) AS 2018_count,
      SUM(CASE WHEN EXTRACT(YEAR FROM txn_date)=2019 THEN 1 END) AS 2019_count,
      SUM(CASE WHEN EXTRACT(YEAR FROM txn_date)=2020 THEN 1 END) AS 2020_count,
      SUM(CASE WHEN EXTRACT(YEAR FROM txn_date)=2021 THEN 1 END) AS 2021_count
    FROM transactions
    GROUP BY ticker
    ORDER BY transactions_count DESC;
    """,
    engine
)

# Solution 2 - With the years on columns:
pd.read_sql_query(
    """
    WITH cte AS (
        SELECT
          *,
          EXTRACT(YEAR FROM txn_date) AS year
        FROM transactions
    )
    SELECT
      ticker,
      year,
      COUNT(*) AS transactions_count
    FROM cte
    GROUP BY ticker, year
    ORDER BY ticker, year ASC;
    """,
    engine
)