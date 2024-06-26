### 0x0E. SQL - More queries

### Resources

* **Read or watch:**

	- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
	- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-administration/mysql-grant/)
	- [MySQL constraints](https://zetcode.com/mysql/constraints/)
	- [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
	- [Basic query operation: the join](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php)
	- [SQL technique: multiple joins and the distinct keyword](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php)
	- [SQL technique: join types](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php)
	- [SQL technique: union and minus](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php)
	- [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
	- [The Seven Types of SQL Joins](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)
	- [MySQL Tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4)
	- [SQL Style Guide](https://www.sqlstyle.guide/)
	- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

* **Extra resources around relational database model design:**

	- [Design](https://www.guru99.com/database-design.html)
	- [Normalization](https://www.guru99.com/database-normalization.html)
	- [ER Modeling](https://www.guru99.com/er-modeling.html)

### Learning Objectives

- At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google:**

* **General**

	- How to create a new MySQL user
	- How to manage privileges for a user to a database or table
	- What’s a `PRIMARY KEY`
	- What’s a `FOREIGN KEY`
	- How to use `NOT NULL` and `UNIQUE` constraints
	- How to retrieve datas from multiple tables in one request
	- What are subqueries
	- What are `JOIN` and `UNION`

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

#### Comments for your SQL file:

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

#### Connect to your MySQL server:

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

**In the container, credentials are** `root/root`

### How to import a SQL dump

```sh
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

## Quiz questions

### Question #0

* Which JOIN type doesn’t exist? (please select all correct answers)

	- [a] **TOP**

	- [b] LEFT

	- [c] INNER

	- [d] FULL OUTER

	- [e] **FULL INNER**

	- [f] **RIGHT AND LEFT**

	- [g] **IN LEFT**

	_**Answers [a], [e], [f], [g]**_

### Question #1

* Is it possible to give only delete access to a table to a user?

	- [a] **Yes**

	- [b] No

	_**Answer [a]**_

### Question #2

* What DCL means?

	- [a] Document Control Line

	- [b] Document Control Language

	- [c] Data Concept Language

	- [d] **Data Control Language**

	_**Answer [d]**_

### Question #3

* Is it possible to give only read access to multiple databases and tables to a user?

	- [a] **Yes**

	- [b] No
	
	_**Answer [a]**_

### Question #4

* Is it possible to give only read access to a database to a user?

	- [a] **Yes**

	- [b] No
	
	_**Answer [a]**_

### Question #5

* Is it possible to give only insert access to a table to a user?

	- [a] **Yes**

	- [b] No

	_**Answer [a]**_

### Question #6

* Is it possible to give only read access to a table to a user?

	- [a] **Yes**

	- [b] No

	_**Answer [a]**_

### Tasks

0. [My privileges!](0-privileges.sql)

* Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`)

```sh
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
ERROR 1141 (42000) at line 3: There is no such grant defined for user 'user_0d_1' on host 'localhost'
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, INSERT, UPDA..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,AUDIT...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'              
guillaume@ubuntu:~/$ 
```

* **Repo:**

	- GitHub repository: `alx-higher_level_programming`
	- Directory: `0x0E-SQL_more_queries`
	- File: `0-privileges.sql`

1. [Root user](1-create_user.sql)

* Write a script that creates the MySQL server user `user_0d_1`.

	- `user_0d_1` should have all privileges on your MySQL server
	- The `user_0d_1` password should be set to `user_0d_1_pwd`
	- If the user `user_0d_1` already exists, your script should not fail

```sh
guillaume@ubuntu:~/$ cat 1-create_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, INSERT..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
guillaume@ubuntu:~/$ 
```

* **Repo:**

	- GitHub repository: `alx-higher_level_programming`
	- Directory: `0x0E-SQL_more_queries`
	- File: `1-create_user.sql`

2. [Read user](2-create_read_user.sql)

* Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`

	- `user_0d_2` should have only SELECT privilege in the database `hbtn_0d_2`
	- The `user_0d_2` password should be set to `user_0d_2_pwd`
	- If the database `hbtn_0d_2` already exists, your script should not fail
	- If the user `user_0d_2` already exists, your script should not fail

```sh
guillaume@ubuntu:~/$ cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, ..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
Grants for user_0d_2@localhost                                                                                                
GRANT USAGE ON *.* TO `user_0d_2`@`localhost`                                                                                 
GRANT SELECT ON `hbtn_0d_2`.* TO `user_0d_2`@`localhost`  
guillaume@ubuntu:~/$ 
```

* **Repo:**

	- GitHub repository: `alx-higher_level_programming`
	- Directory: `0x0E-SQL_more_queries`
	- File: `2-create_read_user.sql`

3. [Always a name](3-force_name.sql)

* Write a script that creates the table force_name on your MySQL server.

	* `force_name` description:
		- `id` INT
		- `name` VARCHAR(256) can’t be null
	- The database name will be passed as an argument of the `mysql` command
	- If the table `force_name` already exists, your script should not fail

```sh
guillaume@ubuntu:~/$ cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO force_name (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ echo 'INSERT INTO force_name (id) VALUES (333);' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
ERROR 1364 (HY000) at line 1: Field 'name' doesn't have a default value
guillaume@ubuntu:~/$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ 
```

* **Repo:**

	- GitHub repository: `alx-higher_level_programming`
	- Directory: `0x0E-SQL_more_queries`
	- File: `3-force_name.sql`

4. [ID can't be null](4-never_empty.sql)

* Write a script that creates the table `id_not_null` on your MySQL server.

	* `id_not_null` description:
		- `id` INT with the default value `1`
		- `name` VARCHAR(256)
	- The database name will be passed as an argument of the `mysql` command
	- If the table `id_not_null` already exists, your script should not fail

```sh
guillaume@ubuntu:~/$ cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO id_not_null (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ echo 'INSERT INTO id_not_null (name) VALUES ("Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
1   Best
guillaume@ubuntu:~/$ 
```

* **Repo:**

	- GitHub repository: `alx-higher_level_programming`
	- Directory: `0x0E-SQL_more_queries`
	- File: `4-never_empty.sql`

5. [Unique ID](5-unique_id.sql)

* Write a script that creates the table `unique_id` on your MySQL server.

	* `unique_id` description:
		- `id` INT with the default value 1 and must be unique
		- `name` VARCHAR(256)
	- The database name will be passed as an argument of the `mysql` command
	- If the table `unique_id` already exists, your script should not fail

```sh
guillaume@ubuntu:~/$ cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry '89' for key 'unique_id.id'
guillaume@ubuntu:~/$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ 
```

* **Repo:**

	- GitHub repository: `alx-higher_level_programming`
	- Directory: `0x0E-SQL_more_queries`
	- File: `5-unique_id.sql`

6. [States table](6-states.sql)

* Write a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server.

	* `states` description:
		- `id` INT unique, auto generated, can’t be null and is a primary key
		- `name` VARCHAR(256) can’t be null
	- If the database `hbtn_0d_usa` already exists, your script should not fail
	- If the table `states` already exists, your script should not fail

```sh
guillaume@ubuntu:~/$ cat 6-states.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   California
2   Arizona
3   Texas
guillaume@ubuntu:~/$ 
```

* **Repo:**

	- GitHub repository: `alx-higher_level_programming`
	- Directory: `0x0E-SQL_more_queries`
	- File: `6-states.sql`

7. [Cities table](7-cities.sql)

* Write a script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server.

	* `cities` description:
		- `id` INT unique, auto generated, can’t be null and is a primary key
		- `state_id` INT, can’t be null and must be a `FOREIGN KEY` that references to `id` of the `states` table
		- `name` VARCHAR(256) can’t be null
	- If the database `hbtn_0d_usa` already exists, your script should not fail
	- If the table `cities` already exists, your script should not fail

```sh
guillaume@ubuntu:~/$ cat 7-cities.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO cities (state_id, name) VALUES (1, "San Francisco");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
guillaume@ubuntu:~/$ echo 'INSERT INTO cities (state_id, name) VALUES (10, "Paris");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
ERROR 1452 (23000) at line 1: Cannot add or update a child row: a foreign key constraint fails (`hbtn_0d_usa`.`cities`, CONSTRAINT `cities_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `states` (`id`))
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
guillaume@ubuntu:~/$ 
```

* **Repo:**

	- GitHub repository: `alx-higher_level_programming`
	- Directory: `0x0E-SQL_more_queries`
	- File: `7-cities.sql`
