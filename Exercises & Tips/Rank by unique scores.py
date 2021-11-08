# Give a rank to scores by ID

"""
Query to create the table for the exercise:

Table Scores:
CREATE TABLE exercises.Scores (
  ID int NOT NULL,
  Score float NOT NULL
);

insert into Scores (ID, Score) values (1, 3.50);
insert into Scores (ID, Score) values (2, 3.65);
insert into Scores (ID, Score) values (3, 4.00);
insert into Scores (ID, Score) values (4, 3.85);
insert into Scores (ID, Score) values (5, 4.00);
insert into Scores (ID, Score) values (6, 3.65);
"""

import pandas as pd
import mysql.connector as sql
import os

connection = sql.connect(
    host = os.environ.get('mysql_host'),
    user = os.environ.get('mysql_user'),
    password = os.environ.get('mysql_password')
)


# Table content:
pd.read_sql_query(
    """
    SELECT *
    FROM exercises.Scores
    """,
    connection
)

# Solution:
pd.read_sql_query(
    """
    SELECT
      Score,
      RANK() OVER(ORDER BY Score DESC)
    FROM exercises.Scores
    """,
    connection
)
# This is not correct, we have to create a table with unique scores to work on.

# Final Solution:
pd.read_sql_query(
    """
    WITH unique_scores AS (
        SELECT d.Score, ROW_NUMBER() OVER(ORDER BY d.Score DESC) AS ScoreRank
        FROM (SELECT DISTINCT Score FROM exercises.Scores) d
    )
    SELECT
      s.Score,
      u.ScoreRank
    FROM exercises.Scores s
    LEFT JOIN unique_scores u
      ON s.Score=u.Score
    ORDER BY s.Score DESC
    """,
    connection
)