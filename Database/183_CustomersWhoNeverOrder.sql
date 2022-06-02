-- report all customers who never order anything

# solution 1: NOT IN
SELECT Name AS Customers FROM Customers c WHERE c.id NOT IN
(SELECT c.id FROM Customers c INNER JOIN Orders o ON c.id = o.customerId);

# solution 2: LEFT JOIN
SELECT c.Name AS Customers FROM Customers c
LEFT JOIN Orders o ON c.Id = o.CustomerId
WHERE o.CustomerId IS null