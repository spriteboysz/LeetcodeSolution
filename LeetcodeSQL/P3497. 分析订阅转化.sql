create database if not exists P3497;
use P3497;

CREATE TABLE if not exists UserActivity (
    user_id INT,
    activity_date DATE,
    activity_type VARCHAR(20),
    activity_duration INT
);
Truncate table UserActivity;
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('1', '2023-01-01', 'free_trial', '45');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('1', '2023-01-02', 'free_trial', '30');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('1', '2023-01-05', 'free_trial', '60');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('1', '2023-01-10', 'paid', '75');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('1', '2023-01-12', 'paid', '90');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('1', '2023-01-15', 'paid', '65');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('2', '2023-02-01', 'free_trial', '55');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('2', '2023-02-03', 'free_trial', '25');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('2', '2023-02-07', 'free_trial', '50');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('2', '2023-02-10', 'cancelled', '0');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('3', '2023-03-05', 'free_trial', '70');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('3', '2023-03-06', 'free_trial', '60');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('3', '2023-03-08', 'free_trial', '80');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('3', '2023-03-12', 'paid', '50');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('3', '2023-03-15', 'paid', '55');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('3', '2023-03-20', 'paid', '85');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('4', '2023-04-01', 'free_trial', '40');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('4', '2023-04-03', 'free_trial', '35');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('4', '2023-04-05', 'paid', '45');
insert into UserActivity (user_id, activity_date, activity_type, activity_duration)
values ('4', '2023-04-07', 'cancelled', '0');


select *
from UserActivity;

select user_id, activity_type, avg(activity_duration)
from UserActivity
group by user_id, activity_type;

select user_id, activity
from (select user_id, activity_type, avg(activity_duration) activity
      from UserActivity
      group by user_id, activity_type) t
where activity_type = 'free_trial';

select user_id, activity
from (select user_id, activity_type, avg(activity_duration) activity
      from UserActivity
      group by user_id, activity_type) t
where activity_type = 'paid';

select t1.user_id, round(t1.activity, 2) trial_avg_duration, round(t2.activity, 2) paid_avg_duration
from (select user_id, activity
      from (select user_id, activity_type, avg(activity_duration) activity
            from UserActivity
            group by user_id, activity_type) t
      where activity_type = 'free_trial') t1
         join (select user_id, activity
               from (select user_id, activity_type, avg(activity_duration) activity
                     from UserActivity
                     group by user_id, activity_type) t
               where activity_type = 'paid') t2 on t1.user_id = t2.user_id
order by user_id;