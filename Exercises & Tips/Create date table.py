import pandas as pd
import mysql.connector as sql
import os

connection = sql.connect(
    host = os.environ.get('mysql_host'),
    user = os.environ.get('mysql_user'),
    password = os.environ.get('mysql_password')
)


# Generate a single date column:
pd.read_sql_query("""
    WITH recursive Date_Ranges AS (
    SELECT '2018-01-01' as Date + interval 1 day
    UNION ALL
    SELECT d.Date + INTERVAL 1 MONTH
    FROM Date_Ranges d
    INNER JOIN (
        SELECT '2018-02-01' as Date + INTERVAL 1 MONTH
        UNION ALL

    )
    WHERE d.Date < '2019-01-01')
    
    SELECT *
    FROM Date_Ranges;
    """,
    connection
    )


pd.read_sql_query("""
    WITH recursive Dates AS (
    SELECT Date, row_number() over (order by (select(1))) AS row_num

    FROM(
        select '2018-11-30' as Date
        union all
        select Date + interval 1 day
        from Date1
        where Date < '2018-12-31')) Dates

   select * from Dates;
    """,
    connection
    )