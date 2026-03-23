create database if not exists P1667;
use P1667;

Create table If Not Exists Users (
    user_id int,
    name varchar(40)
);
Truncate table Users;
insert into Users (user_id, name)
values ('1', 'aLice');
insert into Users (user_id, name)
values ('2', 'bOB');

select *
from Users;

update Users
set name = concat(upper(left(name, 1)), lower(substring(name, 2)));

select u.user_id, concat(upper(left(u.name, 1)), lower(substring(u.name, 2))) name
from Users u
order by u.user_id;