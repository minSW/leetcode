CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
    SELECT max(e1.salary) INTO result
    FROM (
        SELECT DISTINCT salary
        FROM Employee
    ) e1
    WHERE 
        N-1 = (
            SELECT COUNT(1)
            FROM (
                SELECT DISTINCT salary
                FROM Employee
            ) e2
            WHERE e2.salary > e1.salary
        );
    
    RETURN result;
END;
