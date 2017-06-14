# MySQL

## login
```bash
mysql -h localhost -u root -p
```

## Show databases
```mysql
show databases;
```

## Create database
```mysql
create database my_flask_app;
```

## Use database
```mysql
use my_flask_app;
```

## Create table
```mysql
create table user(
  user_id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(64) NOT NULL,
  password VARCHAR(64) NOT NULL,
  PRIMARY KEY(user_id)
);
```

## Verify table
```mysql
show tables;
```

## Insert user
```mysql
insert into user values('', 'username', '12345');
```