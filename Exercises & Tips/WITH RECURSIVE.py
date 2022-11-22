# You can use WITH RECURSIVE to recall a CTE to itself like in recursive functions

"""
WITH RECURSIVE

ThomasReports AS (
  SELECT EmpFullName
  FROM EmployeeTable
  WHERE
    ManagerName = 'Thomas'
  
  UNION ALL

  SELECT e.EmpFullName
  FROM EmployeeTable e
  INNER JOIN ThomasReports t
    ON (
      e.ManagerName = t.EmployeeName
      ) 
)

SELECT *
FROM ThomasReports
"""