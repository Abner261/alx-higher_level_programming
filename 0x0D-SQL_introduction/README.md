### 0x0D. SQL - Introduction

### Resources
#### Read or watch:

- [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
- [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
- [Basic SQL statements: DDL and DML](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php) (no need to read the chapter “Privileges”)
- [Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
- [SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)
- [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
- [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
- [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
- [installing MySQL in Ubuntu 20.04](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)

* **Learning Objectives**

	- At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google:**

* **General**

	- What’s a database
	- What’s a relational database
	- What does SQL stand for
	- What’s MySQL
	- How to create a database in MySQL
	- What does `DDL` and `DML` stand for
	- How to `CREATE` or `ALTER` a table
	- How to `SELECT` data from a table
	- How to `INSERT`, `UPDATE` or `DELETE` data
	- What are `subqueries`
	- How to use MySQL functions

### Requirements

* **General**

	- Allowed editors: `vi`, `vim`, `emacs`
	- All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
	- All your files should end with a new line
	- All your SQL queries should have a comment just before (i.e. syntax above)
	- All your files should start by a comment describing the task
	- All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
	- A `README.md` file, at the root of the folder of the project, is mandatory
	- The length of your files will be tested using `wc`

### More Info

### Comments for your SQL file:

```sh
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

### Install MySQL 8.0 on Ubuntu 20.04 LTS

```sh
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

* **Connect to your MySQL server:**

```sh
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

### Use “container-on-demand” to run MySQL

* **In the container, credentials are** `root/root`

	- Ask for container `Ubuntu 20.04`
	- Connect via SSH
	- OR connect via the Web terminal
	- In the container, you should start MySQL before playing with it:

```sh
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```

* **In the container, credentials are** `root/root`

### Quiz questions

* **Question #0**

	- How do you list all `users` records with `age > 21` in this table?

```sh
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```

[a] SELECT * FROM users WHERE age BETWEEN 21 AND 89;

[b] SELECT * FROM users WHERE age < 21;

[c]  _**SELECT * FROM users WHERE age > 21;**_

[d] SELECT * FROM users WHERE age IS UP TO 21;

 _**solution [c]**_

* **Question #1**

	- How do you delete the `users` record with `id = 89` in this table?

```sh
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```

[a] DELETE FROM users WHERE id IS EQUAL TO 89;

[b] DELETE users WHERE id = 89;

[c] DELETE FROM users;

[d] _**DELETE FROM users WHERE id = 89;**_

  _**solution [d]**_

* **Question #2**

	- How do you list all `users` in this table?

```sh
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```

[a] SELECT ALL users;

[b] DELETE * FROM users;

[c] _**SELECT * FROM users;**_

 _**solution [c]**_

* **Question #3**

	- What does SQL stand for?

		[a] Structured Question Language

		[b] Sequences of Query Logic

		[c] Solid Query Language

		[d] _**Structured Query Language**_

	 	_**solution [d]**_

* **Question #4**

	- How do you change the name of the `users` record with `id = 89` to `Holberton`?

```sh
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```

[a] UPDATE users SET name = “Holberton”;

[b] _**UPDATE users SET name = “Holberton” WHERE id = 89;**_

[c] CHANGE users SET name = “Holberton” WHERE id = 89;

 _**solution [b]**_

* **Question #5**

	- What does DML stand for?

		[a] Document Model Language

		[b] Database Manipulation Language

		[c] _**Data Manipulation Language**_

		[d] Document Manipulation Language

		_**solution [c]**_

* **Question #6**

	- What is a relational database? (please select all correct answers)

		[a] data are organized by tables and indexes

		[b] _**a database**_

		[c] _**data are organized by tables, records and columns**_

		[d] a table containing multiple object representation

		[e] _**a table containing only one object representation**_

		[f] married databases

		[g] _**a collection of data**_

		_**solutions [b], [c], [e] & [g]**_

* **Question #7**

	- How to you add a new record in the table `users`?

```sh
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```

[a] INSERT INTO users (id, name, age) VALUES (2, “Betty”);

[b] INSERT users (id, name, age) VALUES (2, “Betty”, 30);

[c] _**INSERT INTO users (id, name, age) VALUES (2, “Betty”, 30);**_

[d] INSERT INTO users (id, name) VALUES (2, “Betty”, 30);

_**solution [c]**_

* **Question #8**

	- What does DDL stand for?

		[a] Document Data Language

		[b] _**Data Definition Language**_

		[c] Data Document Language

		[d] Database Definition Language

		_**solution [b]**_

## Tasks

0. [List databases](0-list_databases.sql)

- Write a script that lists all databases of your MySQL server.

```sh
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$
```

* **Repo:**

	- GitHub repository: `alx-higher_level_programming`
	- Directory: `0x0D-SQL_introduction`
	- File: `0-list_databases.sql`

1. [Create a database](1-create_database_if_missing.sql)

* Write a script that creates the database `hbtn_0c_0` in your MySQL server.

	- If the database `hbtn_0c_0` already exists, your script should not fail
	- You are not allowed to use the `SELECT` or `SHOW` statements

```sh
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ 
```

* **Repo:**

	- GitHub repository: `alx-higher_level_programming`
	- Directory: `0x0D-SQL_introduction`
	- File: `1-create_database_if_missing.sql`

2. [Delete a database](2-remove_database.sql)

* Write a script that deletes the database `hbtn_0c_0` in your MySQL server.

	- If the database `hbtn_0c_0` doesn’t exist, your script should not fail
	- You are not allowed to use the `SELECT` or `SHOW` statements

```sh
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                                                                                                  
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ 
```

* **Repo:**

	- GitHub repository: `alx-higher_level_programming`
	- Directory: `0x0D-SQL_introduction`
	- File: `2-remove_database.sql`

3. [List tables](3-list_tables.sql)

* Write a script that lists all the tables of a database in your MySQL server.

	- The database name will be passed as argument of `mysql` command (in the following example: `mysql` is the name of the database)

```sh
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password: 
Tables_in_mysql                                                                              
columns_priv                                                                                 
component                                                                                    
db                                                                                           
default_roles                                                                                
engine_cost                                                                                  
func                                                                                         
general_log                                                                                  
global_grants                                                                                
gtid_executed                                                                                
help_category                                                                                
help_keyword                                                                                 
help_relation                                                                                
help_topic                                                                                   
innodb_index_stats                                                                           
innodb_table_stats                                                                           
password_history                                                                             
plugin                                                                                       
procs_priv                                                                                   
proxies_priv                                                                                 
replication_asynchronous_connection_failover                                                 
replication_asynchronous_connection_failover_managed                                         
role_edges                                                                                   
server_cost                                                                                  
servers                                                                                      
slave_master_info                                                                            
slave_relay_log_info                                                                         
slave_worker_info                                                                            
slow_log                                                                                     
tables_priv                                                                                  
time_zone                                                                                    
time_zone_leap_second                                                                        
time_zone_name                                                                               
time_zone_transition                                                                         
time_zone_transition_type                                                                    
user
guillaume@ubuntu:~/$ 
```

* **Repo:**

	- GitHub repository: `alx-higher_level_programming`
	- Directory: `0x0D-SQL_introduction`
	- File: `3-list_tables.sql`
