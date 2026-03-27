create database if not exists P0550;
use P0550;

Create table If Not Exists Activity (
    player_id int,
    device_id int,
    event_date date,
    games_played int
);
Truncate table Activity;
insert into Activity (player_id, device_id, event_date, games_played)
values ('1', '2', '2016-03-01', '5');
insert into Activity (player_id, device_id, event_date, games_played)
values ('1', '2', '2016-03-02', '6');
insert into Activity (player_id, device_id, event_date, games_played)
values ('2', '3', '2017-06-25', '1');
insert into Activity (player_id, device_id, event_date, games_played)
values ('3', '1', '2016-03-02', '0');
insert into Activity (player_id, device_id, event_date, games_played)
values ('3', '4', '2018-07-03', '5');

select *
from Activity;

select player_id, min(event_date) min_date
from Activity
group by player_id;

select count(player_id)
from Activity;

select round(count(*) / (select count(distinct player_id) from Activity), 2) fraction
from Activity a1, (select player_id, min(event_date) min_date from Activity group by player_id) a2
where a1.player_id = a2.player_id and datediff(a1.event_date, a2.min_date) = 1;