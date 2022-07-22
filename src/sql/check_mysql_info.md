### How to know MySQL ip and root info?

***Run MySQL in terminal***

```
$ mysql -u root -p
```
We can see mysql running in terminal ....
```
mysql> 
```
***MySQL info***
run
```
mysql> status
```

or 
```
mysql> \s
```

***Check host***

```
mysql> SHOW VARIABLES WHERE Variable_name = 'hostname';

#output should be 

----------------------
|Variable_name | Value|
-----------------------
| hostname | vision |
-----------------------
1 row in set (0.00 sec)

mysql >

```

***Check port***

```
mysql> SHOW VARIABLES WHERE port = 'port';

#output should be 

----------------------
|port | Value|
-----------------------
| port | 3306 |
-----------------------
1 row in set (0.00 sec)

mysql >

```

***Check connection id***
```
SELECT host FROM information_schema.processlist WHERE ID=connection_id();
```



***Other ways***

```
SELECT SUBSTRING_INDEX(USER(), '@', -1) AS ip,  @@hostname as hostname, @@port as port, DATABASE() as current_database;

SELECT * FROM information_schema.GLOBAL_VARIABLES where VARIABLE_NAME like 'hostname';

SELECT host FROM information_schema.processlist WHERE ID=connection_id();
```

