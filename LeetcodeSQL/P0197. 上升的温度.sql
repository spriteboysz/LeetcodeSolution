create database if not exists P0197;
use P0197;

Create table If Not Exists Weather (
    id int,
    recordDate date,
    temperature int
);
Truncate table Weather;
insert into Weather (id, recordDate, temperature)
values ('1', '2015-01-01', '10');
insert into Weather (id, recordDate, temperature)
values ('2', '2015-01-02', '25');
insert into Weather (id, recordDate, temperature)
values ('3', '2015-01-03', '20');
insert into Weather (id, recordDate, temperature)
values ('4', '2015-01-04', '30');

select *, date_sub(recordDate, INTERVAL 1 day)
from Weather;

select temperature
from Weather
where recordDate = date_sub('2015-01-02', INTERVAL 1 day);

select id
from Weather w1
where temperature > (select temperature from Weather where recordDate = date_sub(w1.recordDate, INTERVAL 1 day));