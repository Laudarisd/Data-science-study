# SIMPLE MYSQL COMMANDS
--------------------------------------

Note: all the command are exucated in `popsql`. It can also be done in terminal.

To connect to popsql:

```
hostname: ....
port:...
database: Table name
```
=====================================================================
### Create Table

```
CREATE TABLE student;
```
will create a table name student.


For more information while creating table, we can write in this way:

```
CREATE TABLE student(
    student_id INT PRIMARY KEY,
    name VARCHAR(20),
    major VARCHAR(20)
);
```
In another way, we can setup PRIMARY KEY in this way

```
CREATE TABLE student PRIMARY KEY student_id;
```

=====================================================================
### Check created data

```
DESCRIBE student
```

This will show created data
=====================================================================

### Rename Table 

```
ALTER TABLE student
RENAME TO new_table_name;
```

=====================================================================

### Add extra column in created data

```
ALTER TABLE studen ADD gpa DECIMAL(3,2);
```

***Add multiple columns***
```
ALTER TABLE table_name
    ADD new_column_name column_definition
    [FIRST | AFTER column_name],
    ADD new_column_name column_definition
    [FIRST | AFTER column_name],
    ...;
Code language: SQL (Structured Query Language) (sql)
```

More examples:
```
ALTER TABLE vehicles
ADD color VARCHAR(50),
ADD note VARCHAR(255);
```
=====================================================================
### Modify a column
```
ALTER TABLE table_name
MODIFY column_name column_definition
[ FIRST | AFTER column_name];    
```

If we want to change column name a NOT NULL then we can do the following:
```
ALTER TABLE student 
MODIFY name VARCHAR(20) NOT NULL;
```


***Modify multiple columns***
```
ALTER TABLE table_name
    MODIFY column_name column_definition
    [ FIRST | AFTER column_name],
    MODIFY column_name column_definition
    [ FIRST | AFTER column_name],
    ...;
```

e.g. we have a table name `vehicles`. We want to modify column `year` and `color` then we can do the following:
```
ALTER TABLE vehicles 
MODIFY year SMALLINT NOT NULL,
MODIFY color VARCHAR(20) NULL AFTER make;
```
In this example:

First, modify the data type of the year column from INT to SMALLINT
Second, modify the color column by setting the maximum length to 20, removing the NOT NULL constraint, and changing its position to appear after the make column.

=====================================================================
### Delete entire data

```
DELETE TABLE student;
```

This will delete entire dataset


***Delete specific column***

```
ALTER TABLE student DROP COLUMN gpa;
```
This will drop `gpa` column from our table.


=====================================================================

### Insert data 
```
INSERT INTO student VALUES (1, 'JACK', 'Biology')
```

This command will insert 3 values in student table. 

***If we don't know attribute***

```
INSERT INTO student (student_id, name) VALUES (1, 'Jack')
```

This comand will insert two values. Since we didn't know remaining attributes, it will automatically insert `NULL` in remaining attributes.

------------------------------------------------------
Let's define new attribute

```
ALTER TABLE studen ADD major VARCHAR(20) UNIQUE;
```

This command will add new attribute in student table. However, we have a rules for entries. We can't insert similar major and lenght is 20 characters.


***If it is given NO NULL***

In attribute insert criteria, if it is given `NO NULL` then there shouldn't be emty entry while inserting entries


***Default criteria***

If we write `DEFAULT 'Undecided' instead of UNIQUE then this will insert `undecided` if the entries are empty

=====================================================================
### Auto increment

```
CREATE TABLE student (
    student_id int NOT NULL AUTO_INCREMENT,
    LastName varchar(20) NOT NULL,
    FirstName varchar(20),
    major CARCHAR(20) NOT NULL,
    gps DECIMALS(3, 2)
    PRIMARY KEY (student_id)
);
```

By default, the starting value for AUTO_INCREMENT is 1, and it will increment by 1 for each new record

=====================================================================

### Update
To update date table 'student'

```
SELECT * FROM student;
UPDATE student
SET 
major = 'Computer'
WHERE student_id = 4;
```

***Update more than one values ***
If we have table `employes`

```
SELECT * FROM employes
UPDATE employes
SET
lastname = 'Hill',
    email = 'mary.hill@classicmodelcars.com'
WHERE
    employeeNumber = 1056;
```
```
UPDATE employees
SET email = REPLACE(email,'@classicmodelcars.com','@mysqltutorial.org')
WHERE
   jobTitle = 'Sales Rep' AND
   officeCode = 6;
```


***Update with more condition***
```
SELECT * FROM student;
UPDATE student
SET 
major = 'Computer'
WHERE major = 'Bio' or major = 'Chem' ;
```

=====================================================================
### Delete row
```
SELECT * FROM student
DELETE FROM student
WHERE student_id = 5;
```
We can also use `and` condition
```
WHERE name = 'TOM' AND major = 'Undecided';
```



[refrence](https://www.w3schools.com/sql/sql_dates.asp)
