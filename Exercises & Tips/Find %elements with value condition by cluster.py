# Given an employee and a department table (they could contain everything else),
# select the top department which consists of the highest percentage of 
# employees who earn over 1500 in salary and have at least 2 employees.

"""
Query to create the tables for the exercise:

Employees table:
CREATE TABLE IF NOT EXISTS employees.employees_exercise(
ID INT(2) NOT NULL,
EmpName varchar(15) NOT NULL,
Salary INT(10) NOT NULL,
DeptID INT(2) NOT NULL
)
;


USE employees;
INSERT INTO employees_exercise (ID, EmpName, Salary, DeptID) VALUES (1, 'Teja', 1100, 1);
INSERT INTO employees_exercise (ID, EmpName, Salary, DeptID) VALUES (2, 'Kura', 2006, 2);
INSERT INTO employees_exercise (ID, EmpName, Salary, DeptID) VALUES (3, 'Sai', 1201, 2);
INSERT INTO employees_exercise (ID, EmpName, Salary, DeptID) VALUES (4, 'Chintu', 5000, 3);
INSERT INTO employees_exercise (ID, EmpName, Salary, DeptID) VALUES (5, 'Mintu', 500, 3);
INSERT INTO employees_exercise (ID, EmpName, Salary, DeptID) VALUES (6, 'Abhi', 2500, 3);

Department table: 
CREATE TABLE IF NOT EXISTS employees.departments_exercise(
DeptID INT(2) NOT NULL,
DeptName varchar(50) NOT NULL
)
;


INSERT INTO departments_exercise (DeptID, DeptName) VALUES (1, 'IT');
INSERT INTO departments_exercise (DeptID, DeptName) VALUES (2, 'HR');
INSERT INTO departments_exercise (DeptID, DeptName) VALUES (3, 'Sales');
"""


import pandas as pd
import mysql.connector as sql
import os

connection = sql.connect(
    host = os.environ.get('mysql_host'),
    user = os.environ.get('mysql_user'),
    password = os.environ.get('mysql_password')
)

# Let's see the tables content:

pd.read_sql_query(
  """
  SELECT *
  FROM employees.employees_exercise
  """,
  connection)

pd.read_sql_query(
  """
  SELECT *
  FROM employees.departments_exercise
  """,
  connection)

# Solution:
pd.read_sql_query(
  """
  SELECT 
    d.DeptName,
    COUNT(DISTINCT ID) AS NumberOfEmployees,
    SUM(CASE WHEN e.Salary > 1500 THEN 1 ELSE 0 END)/COUNT(DISTINCT ID) AS pctAbove1500
  FROM employees.employees_exercise e
  INNER JOIN employees.departments_exercise d
    ON e.DeptID=d.DeptID
  GROUP BY e.DeptID
  HAVING NumberOfEmployees >= 2
  ORDER BY pctAbove1500 DESC
  LIMIT 1
  """,
  connection)