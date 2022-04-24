import pandas as pd
import mysql.connector as sql
import os

connection = sql.connect(
    # host = os.environ.get('mysql_host'),
    host = os.environ.get('mysql_host'),
    user = os.environ.get('mysql_user'),
    password = os.environ.get('mysql_password')
)


# Create a Stored Procedure that selects all rows from "departments" table in "employees" schema:
pd.read_sql_query("""
    DELIMITER //  # the delimiter parameter changes the default delimiter ";" to the one you want 
    USE employees;

    CREATE PROCEDURE SelectAllDepartments()
    BEGIN
        SELECT * FROM departments;
    END //

    DELIMITER ;
    """,
    connection
    )


# Now you can run this stored procedure with the CALL statement:
pd.read_sql_query("""
    CALL SelectAllDepartments();
    """,
    connection
    )

"""
Here is the basic syntax of the CREATE PROCEDURE statement:
CREATE PROCEDURE procedure_name(parameter_list)
BEGIN
   statements;
END //
"""


# References:
# https://www.mysqltutorial.org/getting-started-with-mysql-stored-procedures.aspx