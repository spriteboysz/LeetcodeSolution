create database if not exists P1204;
use P1204;

Create table If Not Exists Queue (
    person_id int,
    person_name varchar(30),
    weight int,
    turn int
);
Truncate table Queue;
insert into Queue (person_id, person_name, weight, turn)
values ('5', 'Alice', '250', '1');
insert into Queue (person_id, person_name, weight, turn)
values ('4', 'Bob', '175', '5');
insert into Queue (person_id, person_name, weight, turn)
values ('3', 'Alex', '350', '2');
insert into Queue (person_id, person_name, weight, turn)
values ('6', 'John Cena', '400', '3');
insert into Queue (person_id, person_name, weight, turn)
values ('1', 'Winston', '500', '6');
insert into Queue (person_id, person_name, weight, turn)
values ('2', 'Marie', '200', '4');

select turn
from Queue
where person_id = 5;

select sum(weight)
from Queue
where turn <= (select turn from Queue where person_id = 5);

select min(turn) - 1
from Queue q1
where (select sum(weight) from Queue where turn <= (select turn from Queue where person_id = q1.person_id)) > 1000;

select person_name
from Queue
where (select min(turn) - 1
       from Queue q1
       where (select sum(weight) from Queue where turn <= (select turn from Queue where person_id = q1.person_id))
               > 1000) = turn;

select *, sum(weight) over(order by turn) as allweight from Queue;

