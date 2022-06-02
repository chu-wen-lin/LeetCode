-- find the employees who earn more than their managers

# solution 1: subquery
SELECT e.name AS Employee FROM Employee AS e
WHERE salary > (
    SELECT salary FROM Employee as m
        WHERE m.id = e.managerId)

# solution 2: INNER JOIN
SELECT e.name AS Employee FROM Employee AS e
    INNER JOIN Employee As m
    ON m.id = e.managerId
    WHERE e.salary > m.salary