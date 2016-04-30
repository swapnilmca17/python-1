#friends_info表单
mysql> create database crawler
    -> ;
Query OK, 1 row affected (0.00 sec)

mysql> create table friends_info(
    -> id int(4) not null primary key,
    -> account_id int(4) not null,
    -> user_name varchar(20) not null,
    -> profile_url varchar(80) not null
    -> );
mysql> desc friends_info;
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| user_id     | int(2)       | NO   | PRI | NULL    |       |
| account_id  | int(10)      | YES  |     | NULL    |       |
| user_name   | varchar(20)  | YES  |     | NULL    |       |
| profile_url | varchar(100) | YES  |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
4 rows in set (0.00 sec)




#profiles_info表单
mysql> create table profiles_info(
    -> id int(4) not null primary key,
    -> name varchar(20),
    -> gender varchar(10),
    -> visits int(8),
    -> level int(4),
    -> log int(4),
    -> album int(4),
    -> posts int(8),
    -> board int(4),
    -> public int(4),
    -> last varchar(40)
    -> );
Query OK, 0 rows affected (0.04 sec)
mysql> desc profiles_info;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| id     | int(4)      | NO   | PRI | NULL    |       |
| name   | varchar(20) | YES  |     | NULL    |       |
| gender | varchar(10) | YES  |     | NULL    |       |
| visits | int(8)      | YES  |     | NULL    |       |
| level  | int(4)      | YES  |     | NULL    |       |
| log    | int(4)      | YES  |     | NULL    |       |
| album  | int(4)      | YES  |     | NULL    |       |
| posts  | int(8)      | YES  |     | NULL    |       |
| board  | int(4)      | YES  |     | NULL    |       |
| public | int(4)      | YES  |     | NULL    |       |
| last   | varchar(40) | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
11 rows in set (0.00 sec)