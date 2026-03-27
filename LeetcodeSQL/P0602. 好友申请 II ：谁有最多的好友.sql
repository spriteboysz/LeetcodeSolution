create database if not exists P0602;
use P0602;

Create table If Not Exists RequestAccepted (
    requester_id int not null,
    accepter_id int null,
    accept_date date null
);
Truncate table RequestAccepted;
insert into RequestAccepted (requester_id, accepter_id, accept_date)
values ('1', '2', '2016/06/03');
insert into RequestAccepted (requester_id, accepter_id, accept_date)
values ('1', '3', '2016/06/08');
insert into RequestAccepted (requester_id, accepter_id, accept_date)
values ('2', '3', '2016/06/08');
insert into RequestAccepted (requester_id, accepter_id, accept_date)
values ('3', '4', '2016/06/09');

select *
from RequestAccepted;

select r1.requester_id a, r1.accepter_id b
from RequestAccepted r1
union
select r2.accepter_id a, r2.requester_id b
from RequestAccepted r2;

select a id, count(*) num
from (select r1.requester_id a, r1.accepter_id b
      from RequestAccepted r1
      union
      select r2.accepter_id a, r2.requester_id b
      from RequestAccepted r2) t
group by id
order by num desc
limit 1;