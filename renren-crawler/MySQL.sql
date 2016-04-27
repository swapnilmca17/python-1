mysql> create database crawler
    -> ;
Query OK, 1 row affected (0.00 sec)

mysql> create table friends_info(
    -> id int(4) not null auto_increment primary key,
    -> account_id int(4) not null,
    -> user_name varchar(20) not null,
    -> profile_url varchar(80) not null,
    -> profile_path varchar(80) not null
    -> );