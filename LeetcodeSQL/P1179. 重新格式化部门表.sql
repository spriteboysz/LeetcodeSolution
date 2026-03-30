create database if not exists P1179;
use P1179;

Create table If Not Exists Department (
    id int,
    revenue int,
    month varchar(5)
);
Truncate table Department;
insert into Department (id, revenue, month)
values ('1', '8000', 'Jan');
insert into Department (id, revenue, month)
values ('2', '9000', 'Jan');
insert into Department (id, revenue, month)
values ('3', '10000', 'Feb');
insert into Department (id, revenue, month)
values ('1', '7000', 'Feb');
insert into Department (id, revenue, month)
values ('1', '6000', 'Mar');

with t01 as (select id, revenue Jan_Revenue from Department where month = 'Jan'),
    t02 as (select id, revenue Feb_Revenue from Department where month = 'Feb'),
    t03 as (select id, revenue Mar_Revenue from Department where month = 'Mar'),
    t04 as (select id, revenue Apr_Revenue from Department where month = 'Apr'),
    t05 as (select id, revenue May_Revenue from Department where month = 'May'),
    t06 as (select id, revenue Jun_Revenue from Department where month = 'Jun'),
    t07 as (select id, revenue Jul_Revenue from Department where month = 'Jul'),
    t08 as (select id, revenue Aug_Revenue from Department where month = 'Aug'),
    t09 as (select id, revenue Sep_Revenue from Department where month = 'Sep'),
    t10 as (select id, revenue Oct_Revenue from Department where month = 'Oct'),
    t11 as (select id, revenue Nov_Revenue from Department where month = 'Nov'),
    t12 as (select id, revenue Dec_Revenue from Department where month = 'Dec')
select distinct d.id, t01.Jan_Revenue, t02.Feb_Revenue, t03.Mar_Revenue, t04.Apr_Revenue, t05.May_Revenue,
    t06.Jun_Revenue, t07.Jul_Revenue, t08.Aug_Revenue, t09.Sep_Revenue, t10.Oct_Revenue, t11.Nov_Revenue,
    t12.Dec_Revenue
from Department d
         left join t01 on d.id = t01.id
         left join t02 on d.id = t02.id
         left join t03 on d.id = t03.id
         left join t04 on d.id = t04.id
         left join t05 on d.id = t05.id
         left join t06 on d.id = t06.id
         left join t07 on d.id = t07.id
         left join t08 on d.id = t08.id
         left join t09 on d.id = t09.id
         left join t10 on d.id = t10.id
         left join t11 on d.id = t11.id
         left join t12 on d.id = t12.id;
