/* Write your PL/SQL query statement below */
WITH NewSeat AS (
    SELECT 
        CASE 
            WHEN mod(id, 2) = 0 THEN id - 1
            ELSE id + 1
        END AS new_id,
        student
    FROM Seat
)
SELECT 
    s.id,
    CASE
        WHEN n.student IS NULL THEN s.student
        ELSE n.student
    END student
FROM Seat s LEFT JOIN NewSeat n ON (s.id = n.new_id)
ORDER BY s.id
