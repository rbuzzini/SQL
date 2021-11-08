"""
Query to create the table for the exercise

USE exercises;
CREATE TABLE exercises.Stadium (
  ID int NOT NULL,
  Date date NOT NULL,
  Visitors int NOT NULL
);

insert into Stadium (ID, Date, Visitors) values (1, '2020-11-12', 10);
insert into Stadium (ID, Date, Visitors) values (2, '2020-11-13', 190);
insert into Stadium (ID, Date, Visitors) values (3, '2020-11-14', 110);
insert into Stadium (ID, Date, Visitors) values (4, '2020-11-15', 98);
insert into Stadium (ID, Date, Visitors) values (5, '2020-11-16', 120);
insert into Stadium (ID, Date, Visitors) values (6, '2020-11-17', 1199);
insert into Stadium (ID, Date, Visitors) values (7, '2020-11-18', 128);
insert into Stadium (ID, Date, Visitors) values (8, '2020-11-20', 728);
"""

# The table is composed by stadiumID, date, number of visitors on that particular
# date.
# The table content is the following:
import pandas as pd
import mysql.connector as sql
import os

connection = sql.connect(
    host = os.environ.get('mysql_host'),
    user = os.environ.get('mysql_user'),
    password = os.environ.get('mysql_password')
)

pd.read_sql_query(
    """
    SELECT *
    FROM exercises.Stadium
    """,
    connection
) 

# Question: display three or more consecutive ID's, having visitors more than 
# or equal to 100, consecutive visiting date and sorted by their visiting date.
#  IDs will be consecutive and unique.

# Solution:
pd.read_sql_query(
    """
    WITH table1 AS (
    SELECT s1.*, DATE_ADD(s1.Date, INTERVAL -ROW_NUMBER() OVER (ORDER BY s1.Date) DAY) AS DateReference
    FROM exercises.Stadium s1, exercises.Stadium s2, exercises.Stadium s3
    WHERE ((s2.ID=s1.ID+1 AND s3.ID=s1.ID+2)
      OR (s1.ID=s2.ID+1 AND s1.ID=s3.ID-1)
      OR (s1.ID=s2.ID+2 AND s1.ID=s3.ID+1))
      AND s1.Visitors>100 AND s2.Visitors>100 AND s3.Visitors>100
    GROUP BY s1.ID
    ORDER BY s1.ID
    )
    SELECT 
      *
    FROM table1
    """, 
    connection
) 




pd.read_sql_query(
    """
    WITH table1 AS (
    SELECT s1.*, DATE_ADD(s1.Date, INTERVAL -ROW_NUMBER() OVER (ORDER BY s1.Date) DAY) AS DateReference
    FROM exercises.Stadium s1, exercises.Stadium s2, exercises.Stadium s3
    WHERE ((s2.ID=s1.ID+1 AND s3.ID=s1.ID+2)
      OR (s1.ID=s2.ID+1 AND s1.ID=s3.ID-1)
      OR (s1.ID=s2.ID+2 AND s1.ID=s3.ID+1))
      AND s1.Visitors>100 AND s2.Visitors>100 AND s3.Visitors>100
    GROUP BY s1.ID
    ORDER BY s1.ID
    ),
    filter_table AS (
    SELECT 
      COUNT(*) AS cnt,
      MIN(Date) AS StartDate,
      MAX(Date) AS EndDate
    FROM table1
    GROUP BY DateReference
    HAVING cnt >=3
    )

    SELECT 
      t.ID,
      t.Date,
      t.Visitors
    FROM table1 t
    INNER JOIN filter_table f
      ON t.Date BETWEEN f.StartDate AND f.EndDate
    ORDER BY t.Date;
    """, 
    connection
) 
