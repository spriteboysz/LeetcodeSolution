create database P0176;
use P0176;

Create table If Not Exists Employee (
    id int,
    salary int
);
Truncate table Employee;
insert into Employee (id, salary)
values ('1', '100');
insert into Employee (id, salary)
values ('2', '200');
insert into Employee (id, salary)
values ('3', '300');

select *
from Employee;

select ifnull((select distinct salary from Employee order by salary desc limit 1, 1), null) AS SecondHighestSalary;

