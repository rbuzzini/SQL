"""
Query to create the tables for the exercise:

Table Accounts:
CREATE TABLE exercises.Accounts (
  AccountID int(2) NOT NULL,
  AccountName varchar(15) NOT NULL
);

insert into Accounts (AccountID, AccountName) values (1, 'Alice');
insert into Accounts (AccountID, AccountName) values (2, 'Bob');
insert into Accounts (AccountID, AccountName) values (3, 'Charlie');



Table Transactions:
CREATE TABLE exercises.Transactions (
  TransactionID int(3) NOT NULL,
  AccountID int(2) NOT NULL,
  StartDate date NOT NULL,
  Amount int(5) NOT NULL
);

insert into Transactions (TransactionID, AccountID, StartDate, Amount) values (1, 1, '2020-01-01', 7000);
insert into Transactions (TransactionID, AccountID, StartDate, Amount) values (2, 1, '2020-01-16', 10000);
insert into Transactions (TransactionID, AccountID, StartDate, Amount) values (3, 1, '2020-01-28', -6000);
insert into Transactions (TransactionID, AccountID, StartDate, Amount) values (4, 2, '2020-02-16', 8000);
insert into Transactions (TransactionID, AccountID, StartDate, Amount) values (5, 3, '2020-01-31', 4000);
insert into Transactions (TransactionID, AccountID, StartDate, Amount) values (6, 3, '2020-01.26', -1000);
insert into Transactions (TransactionID, AccountID, StartDate, Amount) values (7, 3, '2020-02-06', 9000);
insert into Transactions (TransactionID, AccountID, StartDate, Amount) values (8, 3, '2020-02-26', 5000);
"""

import pandas as pd
import mysql.connector as sql
import os

connection = sql.connect(
    host = os.environ.get('mysql_host'),
    user = os.environ.get('mysql_user'),
    password = os.environ.get('mysql_password')
)


# Tables content:
pd.read_sql_query(
    """
    SELECT *
    FROM exercises.Accounts
    """,
    connection
)

pd.read_sql_query(
    """
    SELECT *
    FROM exercises.Transactions
    """,
    connection
)


# We want to return the name and balance of all users having a balance
# greater than 10k

pd.read_sql_query(
    """
    SELECT
      a.AccountName,
      SUM(t.Amount) AS TotalAmount
    FROM exercises.Transactions t
    INNER JOIN exercises.Accounts a
      ON t.AccountID=a.AccountID
    GROUP BY t.AccountID
    HAVING TotalAmount > 10000;
    """,
    connection
)