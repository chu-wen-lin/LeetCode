-- report the names of all the salespersons who did not have any orders related to the company with the name "RED"
#1. LEFT JOIN: find who sold to company "RED"
#2. NOT IN: output who is not in the first query result referred to sales_id

SELECT s.name FROM salesperson s
WHERE s.sales_id NOT IN (
        SELECT o.sales_id FROM orders o
        LEFT JOIN company c ON o.com_id = c.com_id
        WHERE c.name = 'RED');