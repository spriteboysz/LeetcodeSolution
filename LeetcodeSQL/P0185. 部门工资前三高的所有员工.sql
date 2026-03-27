create database if not exists P0185;
use P0185;

Create table If Not Exists Employee (
    id int,
    name varchar(255),
    salary int,
    departmentId int
);
Create table If Not Exists Department (
    id int,
    name varchar(255)
);
Truncate table Employee;
insert into Employee (id, name, salary, departmentId)
values ('1', 'Joe', '85000', '1');
insert into Employee (id, name, salary, departmentId)
values ('2', 'Henry', '80000', '2');
insert into Employee (id, name, salary, departmentId)
values ('3', 'Sam', '60000', '2');
insert into Employee (id, name, salary, departmentId)
values ('4', 'Max', '90000', '1');
insert into Employee (id, name, salary, departmentId)
values ('5', 'Janet', '69000', '1');
insert into Employee (id, name, salary, departmentId)
values ('6', 'Randy', '85000', '1');
insert into Employee (id, name, salary, departmentId)
values ('7', 'Will', '70000', '1');
Truncate table Department;
insert into Department (id, name)
values ('1', 'IT');
insert into Department (id, name)
values ('2', 'Sales');

select *
from Employee;

select distinct departmentId, salary
from Employee
where departmentId = 2
order by salary desc
limit 2, 1;

select d.name Department, e.name Employee, salary as Salary
from Employee e, Department d
where e.departmentId = d.id and departmentId = 1 and
    salary >= (select distinct salary from Employee where departmentId = 1 order by salary desc limit 2, 1);

select d2.name, t.*
from Department d2,
    (select d.name Department, e.name Employee, salary as Salary
     from Employee e, Department d
     where e.departmentId = d.id and departmentId = d2.id and
         salary >= (select distinct salary from Employee where departmentId = d2.id order by salary desc limit 2, 1)) t
where d2.name = t.Department;
