# We will cover:
# 1 - pd.read_sql_table  
# 2 - pd.read_sql_query
# 3 - df.to_sql
# 4 - pd.read_sql (which is just a wrapper for first two methods)

import pandas as pd
import sqlalchemy
import os

# Make sure you have installed also "PyMySQL" package to continue.


# First of all, we have to create a sqlalchemy engine:
host = os.environ.get('mysql_host')
user = os.environ.get('mysql_user')
password = os.environ.get('mysql_password')
engine = sqlalchemy.create_engine(f'mysql+pymysql://{user}:{password}@{host}/exercises')
sql_con = engine.raw_connection()


# Now we can read a table inside "exercises" database with pd.read_sql_table() method.
# It needs these mandatory parameters: table_name and sqlalchemy engine
df = pd.read_sql_table("transactions", engine)
df.head()
# Read pd.read_sql_table documentation to find out possible parameters (like selecting columns etc.)


# Now we can customize the "transactions" dataframe directly with pd.read_sql_query(),
# which requires query parameter
query = '''SELECT TransactionID, Amount
    FROM transactions
    WHERE Amount > 4000
    '''
df_filtered = pd.read_sql_query(query, engine)
df_filtered
# Read pd.read_sql_query() documentation for more info.


# Let's see the reverse operation:
# writing data from dataframe to sql table with the df.to_sql() method

# I have these transactions to insert into sql transactions table:
new_transactions = pd.DataFrame({
    'TransactionID': [9, 10],
    'AccountID': [4, 4],
    'StartDate': ['2020-02-28', '2020-03-01'],
    'Amount': [1000, 3000]
})

new_transactions.to_sql(
    name='transactions',     # sql table name
    con=engine,
    index=False,
    if_exists='append'   # important parameter
)

# And if you want to create a new table, you can simply omit "if_exists" parameter



# now transactions table is updated in your MySQL database:
# Here we see the last method: pd.read_sql(). With this function
# you can read a table and a query too.
pd.read_sql('transactions', engine)
pd.read_sql(query, engine)











# References: https://www.youtube.com/watch?v=M-4EpNdlSuY


