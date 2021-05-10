/* Write your PL/SQL query statement below */
SELECT 
    d.Name as Department, e.Name as Employee, e.Salary as Salary
FROM 
    Employee e, 
    Department d,
    (
        SELECT DepartmentId, max(Salary) as max_salary
        FROM Employee
        GROUP BY DepartmentId
    ) ms
WHERE
    ms.DepartmentId = e.DepartmentId 
    AND ms.max_salary = e.Salary 
    AND e.DepartmentId = d.Id
