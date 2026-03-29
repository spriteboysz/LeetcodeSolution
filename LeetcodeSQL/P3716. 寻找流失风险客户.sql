create database if not exists P3716;
use P3716;

CREATE TABLE if not exists subscription_events (
    event_id INT,
    user_id INT,
    event_date DATE,
    event_type VARCHAR(20),
    plan_name VARCHAR(20),
    monthly_amount DECIMAL(10, 2)
);
Truncate table subscription_events;
insert into subscription_events (event_id, user_id, event_date, event_type, plan_name, monthly_amount)
values ('1', '501', '2024-01-01', 'start', 'premium', '29.99');
insert into subscription_events (event_id, user_id, event_date, event_type, plan_name, monthly_amount)
values ('2', '501', '2024-02-15', 'downgrade', 'standard', '19.99');
insert into subscription_events (event_id, user_id, event_date, event_type, plan_name, monthly_amount)
values ('3', '501', '2024-03-20', 'downgrade', 'basic', '9.99');
insert into subscription_events (event_id, user_id, event_date, event_type, plan_name, monthly_amount)
values ('4', '502', '2024-01-05', 'start', 'standard', '19.99');
insert into subscription_events (event_id, user_id, event_date, event_type, plan_name, monthly_amount)
values ('5', '502', '2024-02-10', 'upgrade', 'premium', '29.99');
insert into subscription_events (event_id, user_id, event_date, event_type, plan_name, monthly_amount)
values ('6', '502', '2024-03-15', 'downgrade', 'basic', '9.99');
insert into subscription_events (event_id, user_id, event_date, event_type, plan_name, monthly_amount)
values ('7', '503', '2024-01-10', 'start', 'basic', '9.99');
insert into subscription_events (event_id, user_id, event_date, event_type, plan_name, monthly_amount)
values ('8', '503', '2024-02-20', 'upgrade', 'standard', '19.99');
insert into subscription_events (event_id, user_id, event_date, event_type, plan_name, monthly_amount)
values ('9', '503', '2024-03-25', 'upgrade', 'premium', '29.99');
insert into subscription_events (event_id, user_id, event_date, event_type, plan_name, monthly_amount)
values ('10', '504', '2024-01-15', 'start', 'premium', '29.99');
insert into subscription_events (event_id, user_id, event_date, event_type, plan_name, monthly_amount)
values ('11', '504', '2024-03-01', 'downgrade', 'standard', '19.99');
insert into subscription_events (event_id, user_id, event_date, event_type, plan_name, monthly_amount)
values ('12', '504', '2024-03-30', 'cancel', NULL, '0.0');
insert into subscription_events (event_id, user_id, event_date, event_type, plan_name, monthly_amount)
values ('13', '505', '2024-02-01', 'start', 'basic', '9.99');
insert into subscription_events (event_id, user_id, event_date, event_type, plan_name, monthly_amount)
values ('14', '505', '2024-02-28', 'upgrade', 'standard', '19.99');
insert into subscription_events (event_id, user_id, event_date, event_type, plan_name, monthly_amount)
values ('15', '506', '2024-01-20', 'start', 'premium', '29.99');
insert into subscription_events (event_id, user_id, event_date, event_type, plan_name, monthly_amount)
values ('16', '506', '2024-03-10', 'downgrade', 'basic', '9.99');

-- 4. 已订阅 至少 60 天
select user_id, datediff(max(event_date), min(event_date)) days_as_subscriber
from subscription_events
group by user_id
having datediff(max(event_date), min(event_date)) >= 60;

-- 已在其订阅历史中 至少进行过一次 降级
select distinct user_id
from subscription_events
where event_type = 'downgrade';

-- 目前有 有效的订阅（他们的最后事件不是 cancel）
select user_id, max(event_date)
from subscription_events
group by user_id;

select user_id, event_type
from subscription_events
where (user_id, event_date) in (select user_id, max(event_date), event_type
                                from subscription_events
                                group by user_id, event_type) and event_type != 'cancel';

-- 他们 目前的订阅费用 低于历史最高订阅费用的 50%
select user_id, max(monthly_amount)
from subscription_events
group by user_id;

select user_id, monthly_amount
from subscription_events
where (user_id, event_date) in (select user_id, max(event_date) from subscription_events group by user_id);

select t1.user_id, t1.amount
from (select user_id, max(monthly_amount) amount from subscription_events group by user_id) t1,
    (select user_id, monthly_amount
     from subscription_events
     where (user_id, event_date) in (select user_id, max(event_date) from subscription_events group by user_id)) t2
where t1.user_id = t2.user_id and t2.monthly_amount < t1.amount * 0.5;


select tt1.user_id, tt4.plan_name current_plan, tt3.monthly_amount current_monthly_amount,
    tt3.amount max_historical_amount, tt1.days_as_subscriber
from (select user_id, datediff(max(event_date), min(event_date)) days_as_subscriber
      from subscription_events
      group by user_id
      having datediff(max(event_date), min(event_date)) >= 60) tt1
         join (select distinct user_id from subscription_events where event_type = 'downgrade') tt2
on tt1.user_id = tt2.user_id
         join (select t1.user_id, t2.monthly_amount, t1.amount
               from (select user_id, max(monthly_amount) amount from subscription_events group by user_id) t1,
                   (select user_id, monthly_amount
                    from subscription_events
                    where (user_id, event_date) in (select user_id, max(event_date)
                                                    from subscription_events
                                                    group by user_id)) t2
               where t1.user_id = t2.user_id and t2.monthly_amount < t1.amount * 0.5) tt3
on tt1.user_id = tt2.user_id and tt2.user_id = tt3.user_id and tt1.user_id = tt3.user_id
         join (select user_id, plan_name
               from subscription_events
               where (user_id, event_date) in (select user_id, max(event_date)
                                               from subscription_events
                                               group by user_id) and event_type != 'cancel') tt4
on tt1.user_id = tt4.user_id and tt2.user_id = tt4.user_id and tt3.user_id = tt4.user_id and tt2.user_id = tt4.user_id
        and tt3.user_id = tt4.user_id and tt1.user_id = tt2.user_id and tt1.user_id = tt3.user_id
        and tt2.user_id = tt3.user_id
order by days_as_subscriber desc, user_id;


# Write your MySQL query statement below
SELECT user_id, max(if(event_end_rank = 1, plan_name, null)) as current_plan,
    max(if(event_end_rank = 1, monthly_amount, null)) as current_monthly_amount,
    max(monthly_amount) as max_historical_amount,
    datediff(max(if(event_end_rank = 1, event_date, null)),
             max(if(event_start_rank = 1, event_date, null))) as days_as_subscriber
FROM (SELECT *, row_number() over (partition by user_id order by event_date desc) as event_end_rank,
          row_number() over (partition by user_id order by event_date ) as event_start_rank
      FROM subscription_events) s
GROUP BY user_id
HAVING max(if(event_end_rank = 1, event_type, null)) <> 'cancel' AND sum(if(event_type = 'downgrade', 1, null)) >= 1 AND
    max(if(event_end_rank = 1, monthly_amount, null)) < max(monthly_amount) / 2 AND
    datediff(max(if(event_end_rank = 1, event_date, null)), max(if(event_start_rank = 1, event_date, null))) >= 60
ORDER BY days_as_subscriber desc, user_id;


