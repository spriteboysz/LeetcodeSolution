create database if not exists P1731;
use P1731;

Create table If Not Exists Employees (
    employee_id int,
    name varchar(20),
    reports_to int,
    age int
);
Truncate table Employees;
insert into Employees (employee_id, name, reports_to, age)
values ('9', 'Hercy', NULL, '43');
insert into Employees (employee_id, name, reports_to, age)
values ('6', 'Alice', '9', '41');
insert into Employees (employee_id, name, reports_to, age)
values ('4', 'Bob', '9', '36');
insert into Employees (employee_id, name, reports_to, age)
values ('2', 'Winston', NULL, '37');

select reports_to, count(*), avg(age) cnt
from Employees
where not isnull(reports_to)
group by reports_to;

select e1.employee_id, e1.name, e2.reports_count, e2.average_age
from (select reports_to, count(*) reports_count, round(avg(age)) average_age
      from Employees
      where not isnull(reports_to)
      group by reports_to) as e2
         left join Employees e1 on e2.reports_to = e1.employee_id
order by e1.employee_id;