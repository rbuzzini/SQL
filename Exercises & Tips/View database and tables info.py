# Importing packages:
import pandas as pd
import os
import sqlalchemy

# Connecting to MySQL database:
host = os.environ.get('mysql_host')
user = os.environ.get('mysql_user')
password = os.environ.get('mysql_password')
engine = sqlalchemy.create_engine(f'mysql+pymysql://{user}:{password}@{host}/pizza_runner')


# To view selected database:
pd.read_sql_query(
    """
    SHOW DATABASES();
    """,
    engine
)


# To view database tables:
pd.read_sql_query(
    """
    SHOW TABLES;
    """,
    engine
)


# To view tables info:
pd.read_sql_query(
    """
    DESCRIBE customer_orders;
    """,
    engine
)

# or
pd.read_sql_query(
    """
    SELECT
      table_name,
      column_name,
      data_type
    FROM information_schema.columns
    WHERE table_name = 'customer_orders';
    """,
    engine
)



