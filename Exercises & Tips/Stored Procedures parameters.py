"""
Often, stored procedures have parameters. 
The parameters make the stored procedure more useful and reusable. 
A parameter in a stored procedure has one of three modes: 
IN, OUT, or INOUT.

Here is the basic syntax of defining a parameter in stored procedures:
'[IN | OUT | INOUT] parameter_name datatype[(length)]'

Let’s take some examples of using stored procedure parameters.
"""

import pandas as pd
import mysql.connector as sql
import os

connection = sql.connect(
    # host = os.environ.get('mysql_host'),
    host = os.environ.get('mysql_host'),
    user = os.environ.get('mysql_user'),
    password = os.environ.get('mysql_password')
)


# 1 - IN parameter example:

# Create a Stored Procedure that selects all orders from "customer_orders" table
# in "pizza_runner" schema during a specific day:
pd.read_sql_query("""
    USE pizza_runner;
    DELIMITER //

    CREATE PROCEDURE GetOrdersByDate(
        IN orderDate DATE
    )
    BEGIN
        SELECT * 
        FROM customer_orders
        WHERE CAST(order_time AS DATE) = orderDate;
    END //

    DELIMITER ;
    """,
    connection
    )


# Now you can run this stored procedure with the CALL statement:
pd.read_sql_query("""
    CALL GetOrdersByDate('2020-01-01');
    """,
    connection
    )

"""
Because the countryName is the IN parameter, you must pass an argument. 
If you don’t do so, you’ll get an error.
"""



# 2 - OUT parameter example:

# Create a store procedure that counts the orders by customer id (it could
# be any qualitative field/cluster):
pd.read_sql_query("""
    USE pizza_runner;
    DELIMITER $$

    CREATE PROCEDURE GetOrdersCountByCustomerID(
        IN customerId varchar(10),
        OUT total INT
    )
    BEGIN
        SELECT
        COUNT(customer_id)
        INTO total
        FROM customer_orders
        WHERE customer_id=customerID;
    END $$

    DELIMITER ;
    """,
    connection
    )



pd.read_sql_query("""
    CALL GetOrdersCountByCustomerID('103', @total);
    SELECT @total;
    """,
    connection
    )



# 3 - INOUT parameter example:

# The following example demonstrates how to use an INOUT parameter in a stored procedure:
pd.read_sql_query("""
    DELIMITER $$

    CREATE PROCEDURE SetCounter(
        INOUT counter INT,
        IN inc INT
    )
    BEGIN
        SET counter = counter + inc;
    END$$

    DELIMITER ;
    """,
    connection
    )

"""
In this example, the stored procedure SetCounter() accepts one INOUT parameter 
( counter ) and one IN parameter ( inc ). It increases the counter ( counter ) 
by the value of specified by the inc parameter.
"""

pd.read_sql_query("""
    SET @counter = 1;
    CALL SetCounter(@counter,1); -- 2
    CALL SetCounter(@counter,1); -- 3
    CALL SetCounter(@counter,5); -- 8
    SELECT @counter; -- 8
    """,
    connection
    )



# References:
# https://www.mysqltutorial.org/stored-procedures-parameters.aspx