create database pydb;

use pydb;

create table song(
	id int(11) not null primary key,
	name varchar(20),
	singer varchar(20),
	path varchar(60)
	);