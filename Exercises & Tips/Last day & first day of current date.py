# There are many ways to get the last day or the first day
# of the current date month


# BigQuery example to retrieve last day of the month date:
# - SELECT LAST_DAY(CURRENT_DATE(), MONTH) AS last_day_of_the_month_date1

# BigQuery examples to retrieve first day of the month date:
# - SELECT DATE_ADD(DATE_ADD(LAST_DAY(CURRENT_DATE(), MONTH), INTERVAL -1 MONTH), INTERVAL 1 DAY) AS first_day_of_the_month_date1
# - SELECT DATE(EXTRACT(YEAR FROM CURRENT_DATE()), EXTRACT(MONTH FROM CURRENT_DATE()), 1) AS first_day_of_the_month_date2