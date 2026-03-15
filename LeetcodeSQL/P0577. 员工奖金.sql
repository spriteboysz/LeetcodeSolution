create database P0577;
use P0577;
;
Create Table If Not Exists Employee (
    EmpId Int,
    Name varchar(255),
    supervisor int,
    salary int
);
Create Table If Not Exists Bonus (
    EmpId Int,
    Bonus Int
);
Truncate Table Employee;
Insert Into Employee (EmpId, Name, Supervisor, Salary)
values ('3', 'Brad', NULL, '4000');
Insert Into Employee (EmpId, Name, Supervisor, Salary)
values ('1', 'John', '3', '1000');
Insert Into Employee (EmpId, Name, Supervisor, Salary)
values ('2', 'Dan', '3', '2000');
Insert Into Employee (EmpId, Name, Supervisor, Salary)
values ('4', 'Thomas', '3', '4000');
Truncate Table Bonus;
Insert Into Bonus (EmpId, Bonus)
Values ('2', '500');
Insert Into Bonus (EmpId, Bonus)
Values ('4', '2000');

select *
from Employee;

select e.name, b.bonus
from Employee e
         left join Bonus b on e.EmpId = b.EmpId
where b.Bonus < 1000 or b.Bonus is null;