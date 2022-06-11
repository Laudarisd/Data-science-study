# SQL commands

## SETUP and Installation



Note: all the command are exucated in `popsql`. It can also be done in terminal.


### Create Table

```
CREATE TABLE student;
```
will create a table name student.


For more information while creating table, we can write in this way:

```
CREATE TABLE student(student_id INT PRIMARY KEY, name VARCHAR(20), major VARCHAR(20));
```
In another way, we can setup PRIMARY KEY in this way

```
CREATE TABLE student PRIMARY KEY student_id;
```


### Check created data

```
DESCRIBE student
```

This will show created data

### Add extra column in created data

```
ALTER TABLE studen ADD gpa DECIMAL(3,2);
```
This will add a new column 'gpa' with decimal criteria  in our table `student`


### Delete entire data

```
DELETE TABLE student;
```

This will delete entire dataset


### Delete specific column

```
ALTER TABLE student DROP COLUMN gpa;
```
This will drop `gpa` column from our table.

### Insert data 
```
INSERT INTO student VALUES (1, 'JACK', 'Biology')
```

This command will insert 3 values in student table. 

### If we don't know attribute

```
INSERT INTO student (student_id, name) VALUES (1, 'Jack')
```

This comand will insert two values. Since we didn't know remaining attributes, it will automatically insert `NULL` in remaining attributes.

--------------------------------------

Let's define new attribute

```
ALTER TABLE studen ADD major VARCHAR(20) UNIQUE;
```

This command will add new attribute in student table. However, we have a rules for entries. We can't insert similar major and lenght is 20 characters.


#### If it is given NO NULL

In attribute insert criteria, if it is given `NO NULL` then there shouldn't be emty entry while inserting entries


### Default criteria

If we write `DEFAULT 'Undecided' instead of UNIQUE then this will insert `undecided` if the entries are empty



