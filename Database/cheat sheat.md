SQL stands for "Structured Query Language".

**Database** provides schemas and metadata that allows for a quick search of the needed data.

A **schema** provides how you organize the data. 

**Metadata** holds structural and statistical information.

---
> ";" is a symbol at the end of the query, NOT the symbol of the break of the line.

General form of filtering by criteria
```mysql
SELECT [list of columns], [list of aggregations] FROM table_name

WHERE [list of conditions]
GROUP BY [list of columns] 
HAVING [list of conditions]
ORDER BY [list of columns (ASC)/DESC];
```
Aggregations: `MIN`, `MAX`, `AVG`, `COUNT`, `SUM`...

---

**Join** clause is used to combine rows from two or more tables, based on a related column between them.

- `INNER JOIN` : returns records that have matching values in both tables
- `NATURAL JOIN` : returns all the attributes of both tables, but only keep one copy of same-name column.
- `LEFT JOIN` : returns all records from the left table, and the matched records from the right table
- `RIGHT JOIN` : returns all records from the right table, and the matched records from the left table
```mysql
SELECT column_name(s) FROM table1
    INNER/LEFT/RIGHT JOIN table2
    ON table1.column_name = table2.column_name
```

---

Operators: `IN`, `LIKE`, `BETWEEN...AND...`(minimum and maximum values are included), `EXISTS`, `IS NULL`, `IS DISTINCT`...
```mysql
SELECT product FROM products
WHERE price IN (10, 12, 14);

# -------------------------------------------
# select all the products except for the price mentioned
SELECT product FROM products
WHERE price NOT IN (10, 12, 14);
```
```mysql
# selects all customers whose name is ending with "a"
SELECT * FROM customers
WHERE customer_name LIKE '%a';

# %: means "between zero and many characters"
# _: represents a single character
```

```mysql
# BETWEEN operator
# below two queries are equivalent

SELECT product FROM products
WHERE price BETWEEN 5 AND 10;

SELECT products FROM products
WHERE price >= 5 AND price <= 10;

# -------------------------------------------
# select all the products outside of the range

SELECT product FROM products
WHERE price NOT BETWEEN  5 AND 10;
```

```mysql
# returns suppliers which supply both milk and cheese
SELECT DISTINCT supplier FROM suppliers AS milk_suppliers
WHERE product = "milk"
AND EXISTS(
    SELECT supplier FROM suppliers
    WHERE product = "cheese" AND supplier = milk_suppliers.supplier);

# returns suppliers which supply only milk but not cheese

SELECT DISTINCT supplier FROM suppliers AS milk_suppliers
WHERE product = "milk"
AND NOT EXISTS(
    SELECT supplier FROM suppliers
    WHERE product = "cheese" AND supplier = milk_suppliers.supplier);
```

---
### Create database

```mysql
CREATE DATABASE database_name;
```
### Create a new table
```mysql
CREATE TABLE table_name
    column_1_name column_1_type NOT NULL,
    column_2_name column_2_type DEFAULT default_value,
    column_n_name column_n_type
    PRIMARY KEY (column_name(s))
    CHECK (column_n_name > specific_value);
```
> 1. Use **NOT NULL** constraints to specify that a column should not store NULL values.
> 2. Use **DEFAULT** to set a default value for a column.
> 3. Use **PRIMARY KEY** to uniquely identifies each record in a table. Must contain UNIQUE values, cannot contain NULL values and consists of single or multiple columns (fields).
> 4. USE **CHECK** to limit the value range that can be placed in a column.
---
### Insert new records
```mysql
INSERT INTO table_name (column_1, ..., column_n)
VALUES (value_1, ..., value_n);
```
---
> Arithmetic or string expressions with NULL among the operands are evaluated as NULL.
>
> For example, 2 + 2 * NULL = NULL







