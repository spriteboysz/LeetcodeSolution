create database if not exists P0627;
use P0627;

Create table If Not Exists Salary (
    id int,
    name varchar(100),
    sex char(1),
    salary int
);
Truncate table Salary;
insert into Salary (id, name, sex, salary)
values ('1', 'A', 'm', '2500');
insert into Salary (id, name, sex, salary)
values ('2', 'B', 'f', '1500');
insert into Salary (id, name, sex, salary)
values ('3', 'C', 'm', '5500');
insert into Salary (id, name, sex, salary)
values ('4', 'D', 'f', '500');

select *
from Salary;

-- 编写一个解决方案来交换所有的 'f' 和 'm' （即，将所有 'f' 变为 'm' ，反之亦然），仅使用 单个 update 语句 ，且不产生中间临时表。
update Salary
set sex = case sex when 'm' then 'f' when 'f' then 'm' end;

