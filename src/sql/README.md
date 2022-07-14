# SQL commands

## SETUP and Installation
1. Mac M1 -- Microsoft Azure SQL

Lots of application are still not compatiable in M1 chips device. 
So lets give a try to set up `Microsoft Azure SQL edge`.

- Download Azure Data Studio from (here)[https://docs.microsoft.com/en-us/sql/azure-data-studio/download-azure-data-studio?view=sql-server-ver15#macos-installation]

- Set up docker. To install docker click (here)[https://docs.docker.com/desktop/mac/apple-silicon/]

- Let's pull azure sql edge. In Mac terminal run following command:
```
docker pull mcr.microsoft.com/azure-sql-edge
```
Again run follwoing comand to setup pw and port

```
docker run --cap-add SYS_PTRACE -e ‘ACCEPT_EULA=1’ -e ‘MSSQL_SA_PASSWORD=reallyStrongPwd123@’ -p 1433:1433 --name SQLServer -d mcr.microsoft.com/azure-sql-edge
```

Once the command is run successfully, go back to your mac docker app where we can see `azure...` container.

Now launch Azure Data Studio and click New Connection for setting up the SQL Connection.

- go to new connection
- then on screen :
     > connection name : Microsoft SQL Server
     > server localhost
     > Athentication type : SQL Login
     > User name: sa
     > password: reallyStrongPwd123@
     
- hit connect 

>=== Voila >====

we can see SQL server running on.....

=============================================================


2. My SQL

To install in mac m1: 
```
brew install mysql
```

Start and stop MySQL

```
Start MySQL – sudo mysql.server start
Stop MySQL – sudo mysql.server stop
Restart MySQL – sudo mysql.server restart
Check status – sudo mysql.server status
```

To uninstall MySQL
```
brew uninstall mysql
```

*** How to reset root password in mysql m1 mac
```
Make sure you have Stopped MySQL first (above).
Run the server in safe mode with privilege bypass: sudo mysqld_safe --skip-grant-tables
mysql -u root
UPDATE mysql.user SET authentication_string=null WHERE User='root';
FLUSH PRIVILEGES;
exit;
Then
mysql -u root
ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'yourpasswd';
```
--------------------------------------

Note: all the command are exucated in `popsql`. It can also be done in terminal.

To connect to popsql:

```
hostname: ....
port:...
database: Table name
```
=========================================================
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

--------------------------------------------------------------------------------------




[refrence](https://www.w3schools.com/sql/sql_dates.asp)
