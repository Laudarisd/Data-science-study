### How to know MySQL ip and root info?

***Run MySQL in terminal***

```
$ mysql -u root -p
```
We can see mysql running in terminal ....
```
mysql> 
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