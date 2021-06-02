/* Write your PL/SQL query statement below */
SELECT c.Name as "Customers"
FROM Customers c
WHERE c.Id NOT IN (SELECT o.CustomerId FROM Orders o)

