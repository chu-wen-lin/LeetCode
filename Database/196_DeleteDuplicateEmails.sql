--  Please write a DELETE statement and DO NOT write a SELECT statement.
--  Write your MySQL query statement below


--  Error: You can't specify target table 'Person' for update in FROM clause
--  DELETE FROM Person
--  WHERE id NOT IN
--      (SELECT MIN(id) FROM Person GROUP BY email);

--  solution 1:
DELETE p1 FROM Person p1, Person p2
WHERE p1.Email = p2.Email AND p1.id > p2.id;

--  solution 2:
DELETE p1.* FROM Person p1
JOIN Person p2
ON p1.Email = p2.Email
where p1.id > p2.id;