create database if not exists P3808;
use P3808;

CREATE TABLE reactions (
    user_id INT,
    content_id INT,
    reaction VARCHAR(255)
);

Truncate table reactions;
insert into reactions (user_id, content_id, reaction)
values ('1', '101', 'like');
insert into reactions (user_id, content_id, reaction)
values ('1', '102', 'like');
insert into reactions (user_id, content_id, reaction)
values ('1', '103', 'like');
insert into reactions (user_id, content_id, reaction)
values ('1', '104', 'wow');
insert into reactions (user_id, content_id, reaction)
values ('1', '105', 'like');
insert into reactions (user_id, content_id, reaction)
values ('2', '201', 'like');
insert into reactions (user_id, content_id, reaction)
values ('2', '202', 'wow');
insert into reactions (user_id, content_id, reaction)
values ('2', '203', 'sad');
insert into reactions (user_id, content_id, reaction)
values ('2', '204', 'like');
insert into reactions (user_id, content_id, reaction)
values ('2', '205', 'wow');
insert into reactions (user_id, content_id, reaction)
values ('3', '301', 'love');
insert into reactions (user_id, content_id, reaction)
values ('3', '302', 'love');
insert into reactions (user_id, content_id, reaction)
values ('3', '303', 'love');
insert into reactions (user_id, content_id, reaction)
values ('3', '304', 'love');
insert into reactions (user_id, content_id, reaction)
values ('3', '305', 'love');

select *
from reactions;

select user_id, count(distinct content_id) cnt
from reactions
group by user_id
having cnt >= 5;

select user_id, reaction, count(*) cnt
from reactions
group by user_id, reaction;

select t1.user_id, t2.reaction dominant_reaction, round(t2.cnt / t1.cnt, 2) reaction_ratio
from (select user_id, count(distinct content_id) cnt from reactions group by user_id having cnt >= 5) t1,
    (select user_id, reaction, count(*) cnt from reactions group by user_id, reaction) t2
where t1.user_id = t2.user_id and round(t2.cnt / t1.cnt, 2) >= 0.6
order by reaction_ratio desc, user_id;