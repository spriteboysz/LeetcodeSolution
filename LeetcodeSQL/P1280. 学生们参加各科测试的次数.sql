create database if not exists P1280;
use P1280;

Create table If Not Exists Students (
    student_id int,
    student_name varchar(20)
);
Create table If Not Exists Subjects (
    subject_name varchar(20)
);
Create table If Not Exists Examinations (
    student_id int,
    subject_name varchar(20)
);
Truncate table Students;
insert into Students (student_id, student_name)
values ('1', 'Alice');
insert into Students (student_id, student_name)
values ('2', 'Bob');
insert into Students (student_id, student_name)
values ('13', 'John');
insert into Students (student_id, student_name)
values ('6', 'Alex');
Truncate table Subjects;
insert into Subjects (subject_name)
values ('Math');
insert into Subjects (subject_name)
values ('Physics');
insert into Subjects (subject_name)
values ('Programming');
Truncate table Examinations;
insert into Examinations (student_id, subject_name)
values ('1', 'Math');
insert into Examinations (student_id, subject_name)
values ('1', 'Physics');
insert into Examinations (student_id, subject_name)
values ('1', 'Programming');
insert into Examinations (student_id, subject_name)
values ('2', 'Programming');
insert into Examinations (student_id, subject_name)
values ('1', 'Physics');
insert into Examinations (student_id, subject_name)
values ('1', 'Math');
insert into Examinations (student_id, subject_name)
values ('13', 'Math');
insert into Examinations (student_id, subject_name)
values ('13', 'Programming');
insert into Examinations (student_id, subject_name)
values ('13', 'Physics');
insert into Examinations (student_id, subject_name)
values ('2', 'Math');
insert into Examinations (student_id, subject_name)
values ('1', 'Math');

-- t1
select s1.student_id, s1.student_name, s.subject_name
from Students s1, Subjects s;

create view v1 as
select s1.student_id, s1.student_name, s.subject_name
from Students s1, Subjects s;

-- t2
select s2.student_id, e.subject_name, count(*) as cnt
from Examinations e
         join Students s2 on e.student_id = s2.student_id
group by s2.student_id, s2.student_name, e.subject_name;

drop view v2;
create view v2 as
select s2.student_id, e.subject_name, count(*) as cnt
from Examinations e
         join Students s2 on e.student_id = s2.student_id
group by s2.student_id, s2.student_name, e.subject_name;

select v1.student_id, v1.student_name, v1.subject_name, ifnull(v2.cnt, 0) attended_exams
from v1
         left join v2 on v1.student_id = v2.student_id and v1.subject_name = v2.subject_name
order by v1.student_id, v1.subject_name;

select t1.student_id, t1.student_name, t1.subject_name, ifnull(t2.attended_exams, 0) attended_exams
from (select s1.student_id, s1.student_name, s.subject_name from Students s1, Subjects s) as t1
         left join (select s2.student_id, e.subject_name, count(*) as attended_exams
                    from Examinations e
                             join Students s2 on e.student_id = s2.student_id
                    group by s2.student_id, s2.student_name, e.subject_name) as t2
on t1.student_id = t2.student_id and t1.subject_name = t2.subject_name
order by t1.student_id, t1.subject_name;

-- 视图解
create view v1 as
select s1.student_id, s1.student_name, s.subject_name
from Students s1, Subjects s;

create view v2 as
select s2.student_id, e.subject_name, count(*) as cnt
from Examinations e
         join Students s2 on e.student_id = s2.student_id
group by s2.student_id, s2.student_name, e.subject_name;

select v1.student_id, v1.student_name, v1.subject_name, ifnull(v2.cnt, 0) attended_exams
from v1
         left join v2 on v1.student_id = v2.student_id and v1.subject_name = v2.subject_name
order by v1.student_id, v1.subject_name;
