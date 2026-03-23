create database if not exists P0178;
use P0178;

Create table If Not Exists Scores (
    id int,
    score DECIMAL(3, 2)
);
Truncate table Scores;
insert into Scores (id, score)
values ('1', '3.5');
insert into Scores (id, score)
values ('2', '3.65');
insert into Scores (id, score)
values ('3', '4.0');
insert into Scores (id, score)
values ('4', '3.85');
insert into Scores (id, score)
values ('5', '4.0');
insert into Scores (id, score)
values ('6', '3.65');

select score, count(*)
from Scores
group by score
order by score desc;

select t1.score, (@index := @index + 1) as `rank`
from (select score, count(*) from Scores group by score order by score desc) t1, (select @index := 0) t2;

select t3.score, t4.`rank`
from Scores t3,
    (select t1.score, (@index := @index + 1) as `rank`
     from (select score, count(*) from Scores group by score order by score desc) t1, (select @index := 0) t2) t4
where t3.score = t4.score
order by t3.score desc;