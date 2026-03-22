create database if not exists P1907;
use P1907;

Create table If Not Exists Accounts (
    account_id int,
    income int
);
Truncate table Accounts;
insert into Accounts (account_id, income)
values ('3', '108939');
insert into Accounts (account_id, income)
values ('2', '12747');
insert into Accounts (account_id, income)
values ('8', '87709');
insert into Accounts (account_id, income)
values ('6', '91796');

select *
from Accounts;

select count(*)
from Accounts
where income < 20000;
select count(*)
from Accounts
where income >= 20000 and income <= 50000;
select count(*)
from Accounts
where income > 50000;

select 'Low Salary' category, (select count(*) from Accounts where income < 20000) accounts_count
union
select 'Average Salary' category,
        (select count(*) from Accounts where income >= 20000 and income <= 50000) accounts_count
union
select 'High Salary' category, (select count(*) from Accounts where income > 50000) accounts_count;