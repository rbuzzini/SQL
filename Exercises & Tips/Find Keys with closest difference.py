"""
Query to create the table for the exercise:

CREATE TABLE IF NOT EXISTS employees.students(
ID INT(2) NOT NULL,
StudentName varchar(15) NOT NULL,
Score INT(4) NOT NULL
)
;



INSERT INTO students (ID, StudentName, Score) VALUES (1, 'Teja', 311);
INSERT INTO students (ID, StudentName, Score) VALUES (2, 'Kura', 321);
INSERT INTO students (ID, StudentName, Score) VALUES (3, 'Sai', 317);
INSERT INTO students (ID, StudentName, Score) VALUES (4, 'Chintu', 322);
"""


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
  SELECT s1.StudentName AS Name1,s2.StudentName AS Name2, abs(s1.Score-s2.Score) as diff
  FROM employees.students s1
  INNER JOIN employees.students s2
    ON s1.ID!=s2.ID
  ORDER BY diff ASC
  LIMIT 1
  """,
  connection)
