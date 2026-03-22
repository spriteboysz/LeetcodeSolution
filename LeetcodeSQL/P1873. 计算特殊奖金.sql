create database if not exists P1873;
use P1873;

Create table If Not Exists Employees (
    employee_id int,
    name varchar(30),
    salary int
);
Truncate table Employees;
insert into Employees (employee_id, name, salary)
values ('2', 'Meir', '3000');
insert into Employees (employee_id, name, salary)
values ('3', 'Michael', '3800');
insert into Employees (employee_id, name, salary)
values ('7', 'Addilyn', '7400');
insert into Employees (employee_id, name, salary)
values ('8', 'Juan', '6100');
insert into Employees (employee_id, name, salary)
values ('9', 'Kannon', '7700');

select employee_id, salary * if((employee_id % 2 = 0 or name like 'M%'), 0, 1) bonus
from Employees
order by employee_id;