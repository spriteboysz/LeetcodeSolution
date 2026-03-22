create database if not exists P0196;
use P0196;

Create table If Not Exists Person (
    Id int,
    Email varchar(255)
);
Truncate table Person;
insert into Person (id, email)
values ('1', 'john@example.com');
insert into Person (id, email)
values ('2', 'bob@example.com');
insert into Person (id, email)
values ('3', 'john@example.com');

select min(Id)
from Person
group by Email;

delete a
from Person a
         inner join Person b
where a.Email = b.Email and a.ID > b.ID;

delete
from Person
where id not in (select id from (select min(id) id from Person group by email) t);


select *
from Person;