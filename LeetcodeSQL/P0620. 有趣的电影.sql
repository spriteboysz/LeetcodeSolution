create database P0620;
use P0620;

Create table If Not Exists cinema (
    id int,
    movie varchar(255),
    description varchar(255),
    rating float(2, 1)
);
Truncate table cinema;
insert into cinema (id, movie, description, rating)
values ('1', 'War', 'great 3D', '8.9');
insert into cinema (id, movie, description, rating)
values ('2', 'Science', 'fiction', '8.5');
insert into cinema (id, movie, description, rating)
values ('3', 'irish', 'boring', '6.2');
insert into cinema (id, movie, description, rating)
values ('4', 'Ice song', 'Fantacy', '8.6');
insert into cinema (id, movie, description, rating)
values ('5', 'House card', 'Interesting', '9.1');

-- 编写解决方案，找出所有影片描述为 非 boring (不无聊) 的并且 id 为奇数 的影片。
-- 返回结果按 rating 降序排列
select *
from cinema
where description != 'boring' and id % 2 = 1
order by rating desc;