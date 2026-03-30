create database if not exists P3586;
use P3586;

CREATE TABLE patients (
    patient_id INT,
    patient_name VARCHAR(255),
    age INT
);
CREATE TABLE covid_tests (
    test_id INT,
    patient_id INT,
    test_date DATE,
    result VARCHAR(50)
);
Truncate table patients;
insert into patients (patient_id, patient_name, age)
values ('1', 'Alice Smith', '28');
insert into patients (patient_id, patient_name, age)
values ('2', 'Bob Johnson', '35');
insert into patients (patient_id, patient_name, age)
values ('3', 'Carol Davis', '42');
insert into patients (patient_id, patient_name, age)
values ('4', 'David Wilson', '31');
insert into patients (patient_id, patient_name, age)
values ('5', 'Emma Brown', '29');
Truncate table covid_tests;
insert into covid_tests (test_id, patient_id, test_date, result)
values ('1', '1', '2023-01-15', 'Positive');
insert into covid_tests (test_id, patient_id, test_date, result)
values ('2', '1', '2023-01-25', 'Negative');
insert into covid_tests (test_id, patient_id, test_date, result)
values ('3', '2', '2023-02-01', 'Positive');
insert into covid_tests (test_id, patient_id, test_date, result)
values ('4', '2', '2023-02-05', 'Inconclusive');
insert into covid_tests (test_id, patient_id, test_date, result)
values ('5', '2', '2023-02-12', 'Negative');
insert into covid_tests (test_id, patient_id, test_date, result)
values ('6', '3', '2023-01-20', 'Negative');
insert into covid_tests (test_id, patient_id, test_date, result)
values ('7', '3', '2023-02-10', 'Positive');
insert into covid_tests (test_id, patient_id, test_date, result)
values ('8', '3', '2023-02-20', 'Negative');
insert into covid_tests (test_id, patient_id, test_date, result)
values ('9', '4', '2023-01-10', 'Positive');
insert into covid_tests (test_id, patient_id, test_date, result)
values ('10', '4', '2023-01-18', 'Positive');
insert into covid_tests (test_id, patient_id, test_date, result)
values ('11', '5', '2023-02-15', 'Negative');
insert into covid_tests (test_id, patient_id, test_date, result)
values ('12', '5', '2023-02-20', 'Negative');

select *
from covid_tests;

select patient_id, result, min(if(result = 'Positive', test_date, Null)) positive,
    max(if(result = 'Negative', test_date, Null)) negative
from covid_tests
where result = 'Positive' or result = 'Negative'
group by patient_id, result;


select patient_id, datediff(min(negative), min(positive)) recovery_time
from (select patient_id, result, min(if(result = 'Positive', test_date, Null)) positive,
          max(if(result = 'Negative', test_date, Null)) negative
      from covid_tests
      where (result = 'Positive' or result = 'Negative')
      group by patient_id, result) t
group by patient_id;

select p.*, t2.recovery_time
from patients p
         join (select patient_id, datediff(min(negative), min(positive)) recovery_time
               from (select patient_id, result, min(if(result = 'Positive', test_date, Null)) positive,
                         max(if(result = 'Negative', test_date, Null)) negative
                     from covid_tests
                     where result = 'Positive' or result = 'Negative'
                     group by patient_id, result) t
               group by patient_id) t2 on p.patient_id = t2.patient_id
where recovery_time > 0
order by recovery_time, patient_name;


with t1 as (select patient_id, min(test_date) as positive
            from covid_tests
            where result = 'Positive'
            group by patient_id),
    t2 as (select c.patient_id, min(test_date) as negative
           from covid_tests c
                    join t1 on c.patient_id = t1.patient_id
           where result = 'Negative' and test_date > t1.positive
           group by c.patient_id)

select t1.patient_id, patient_name, age, datediff(t2.negative, t1.positive) as recovery_time
from t1
         join t2 on t1.patient_id = t2.patient_id
         join patients p on p.patient_id = t1.patient_id
order by recovery_time, patient_name;

