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

