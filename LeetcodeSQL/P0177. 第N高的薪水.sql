create database P0177;

use P0177;

Create table If Not Exists Employee (
    Id int,
    Salary int
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

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N := N - 1;
    RETURN (SELECT distinct salary FROM Employee ORDER BY salary DESC LIMIT N, 1);
END;

select getNthHighestSalary(2);

