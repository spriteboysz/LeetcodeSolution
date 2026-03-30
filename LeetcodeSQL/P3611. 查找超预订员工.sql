create database if not exists P3611;
use P3611;

CREATE TABLE if not exists employees (
    employee_id INT,
    employee_name VARCHAR(255),
    department VARCHAR(100)
);
CREATE TABLE meetings (
    meeting_id INT,
    employee_id INT,
    meeting_date DATE,
    meeting_type VARCHAR(50),
    duration_hours DECIMAL(4, 2)
);
Truncate table employees;
insert into employees (employee_id, employee_name, department)
values ('1', 'Alice Johnson', 'Engineering');
insert into employees (employee_id, employee_name, department)
values ('2', 'Bob Smith', 'Marketing');
insert into employees (employee_id, employee_name, department)
values ('3', 'Carol Davis', 'Sales');
insert into employees (employee_id, employee_name, department)
values ('4', 'David Wilson', 'Engineering');
insert into employees (employee_id, employee_name, department)
values ('5', 'Emma Brown', 'HR');
Truncate table meetings;
insert into meetings (meeting_id, employee_id, meeting_date, meeting_type, duration_hours)
values ('1', '1', '2023-06-05', 'Team', '8.0');
insert into meetings (meeting_id, employee_id, meeting_date, meeting_type, duration_hours)
values ('2', '1', '2023-06-06', 'Client', '6.0');
insert into meetings (meeting_id, employee_id, meeting_date, meeting_type, duration_hours)
values ('3', '1', '2023-06-07', 'Training', '7.0');
insert into meetings (meeting_id, employee_id, meeting_date, meeting_type, duration_hours)
values ('4', '1', '2023-06-12', 'Team', '12.0');
insert into meetings (meeting_id, employee_id, meeting_date, meeting_type, duration_hours)
values ('5', '1', '2023-06-13', 'Client', '9.0');
insert into meetings (meeting_id, employee_id, meeting_date, meeting_type, duration_hours)
values ('6', '2', '2023-06-05', 'Team', '15.0');
insert into meetings (meeting_id, employee_id, meeting_date, meeting_type, duration_hours)
values ('7', '2', '2023-06-06', 'Client', '8.0');
insert into meetings (meeting_id, employee_id, meeting_date, meeting_type, duration_hours)
values ('8', '2', '2023-06-12', 'Training', '10.0');
insert into meetings (meeting_id, employee_id, meeting_date, meeting_type, duration_hours)
values ('9', '3', '2023-06-05', 'Team', '4.0');
insert into meetings (meeting_id, employee_id, meeting_date, meeting_type, duration_hours)
values ('10', '3', '2023-06-06', 'Client', '3.0');
insert into meetings (meeting_id, employee_id, meeting_date, meeting_type, duration_hours)
values ('11', '4', '2023-06-05', 'Team', '25.0');
insert into meetings (meeting_id, employee_id, meeting_date, meeting_type, duration_hours)
values ('12', '4', '2023-06-19', 'Client', '22.0');
insert into meetings (meeting_id, employee_id, meeting_date, meeting_type, duration_hours)
values ('13', '5', '2023-06-05', 'Training', '2.0');

select *
from meetings;

select employee_id, yearweek(meeting_date, 1) week
from meetings
group by employee_id, week
having sum(duration_hours) > 20;

select employee_id, count(*) cnt
from (select employee_id, yearweek(meeting_date, 1) week
      from meetings
      group by employee_id, week
      having sum(duration_hours) > 20) t
group by employee_id;

with t as (select employee_id, yearweek(meeting_date, 1) week
           from meetings
           group by employee_id, week
           having sum(duration_hours) > 20)
select t1.employee_id, e.employee_name, e.department, t1.meeting_heavy_weeks
from (select employee_id, count(*) meeting_heavy_weeks from t group by employee_id) t1, employees e
where t1.employee_id = e.employee_id and t1.meeting_heavy_weeks >= 2
order by t1.meeting_heavy_weeks desc, e.employee_name;