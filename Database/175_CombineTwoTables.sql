-- report the first name, last name, city, and state of each person in the Person table

SELECT firstName, lastName, city, state from Person
    LEFT JOIN Address ON Person.personId = Address.personId

