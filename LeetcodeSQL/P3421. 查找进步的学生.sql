create database if not exists P3421;
use P3421;

CREATE TABLE Scores (
    student_id INT,
    subject VARCHAR(50),
    score INT,
    exam_date VARCHAR(10)
);
Truncate table Scores;
insert into Scores (student_id, subject, score, exam_date)
values ('101', 'Math', '70', '2023-01-15');
insert into Scores (student_id, subject, score, exam_date)
values ('101', 'Math', '85', '2023-02-15');
insert into Scores (student_id, subject, score, exam_date)
values ('101', 'Physics', '65', '2023-01-15');
insert into Scores (student_id, subject, score, exam_date)
values ('101', 'Physics', '60', '2023-02-15');
insert into Scores (student_id, subject, score, exam_date)
values ('102', 'Math', '80', '2023-01-15');
insert into Scores (student_id, subject, score, exam_date)
values ('102', 'Math', '85', '2023-02-15');
insert into Scores (student_id, subject, score, exam_date)
values ('103', 'Math', '90', '2023-01-15');
insert into Scores (student_id, subject, score, exam_date)
values ('104', 'Physics', '75', '2023-01-15');
insert into Scores (student_id, subject, score, exam_date)
values ('104', 'Physics', '85', '2023-02-15');

select *
from Scores;

select score
from Scores
where exam_date = '2023-01-15' and student_id = '101';

with t1 as (select student_id, subject, min(exam_date) min_date, max(exam_date) max_date
            from Scores
            group by student_id, subject
            having count(exam_date) > 1)
select s1.student_id, s1.subject, s1.score first_score, s2.score latest_score
from t1
         left join Scores s1 on t1.subject = s1.subject and t1.student_id = s1.student_id and s1.exam_date = t1.min_date
         left join Scores s2 on t1.subject = s2.subject and t1.student_id = s2.student_id and s2.exam_date = t1.max_date
where s1.score < s2.score
order by student_id, subject;