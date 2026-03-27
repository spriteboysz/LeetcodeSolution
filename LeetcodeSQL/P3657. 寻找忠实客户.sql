create database if not exists P3657;
use P3657;

CREATE TABLE if not exists customer_transactions (
    transaction_id INT,
    customer_id INT,
    transaction_date DATE,
    amount DECIMAL(10, 2),
    transaction_type VARCHAR(20)
);
Truncate table customer_transactions;
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type)
values ('1', '101', '2024-01-05', '150.0', 'purchase');
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type)
values ('2', '101', '2024-01-15', '200.0', 'purchase');
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type)
values ('3', '101', '2024-02-10', '180.0', 'purchase');
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type)
values ('4', '101', '2024-02-20', '250.0', 'purchase');
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type)
values ('5', '102', '2024-01-10', '100.0', 'purchase');
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type)
values ('6', '102', '2024-01-12', '120.0', 'purchase');
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type)
values ('7', '102', '2024-01-15', '80.0', 'refund');
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type)
values ('8', '102', '2024-01-18', '90.0', 'refund');
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type)
values ('9', '102', '2024-02-15', '130.0', 'purchase');
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type)
values ('10', '103', '2024-01-01', '500.0', 'purchase');
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type)
values ('11', '103', '2024-01-02', '450.0', 'purchase');
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type)
values ('12', '103', '2024-01-03', '400.0', 'purchase');
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type)
values ('13', '104', '2024-01-01', '200.0', 'purchase');
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type)
values ('14', '104', '2024-02-01', '250.0', 'purchase');
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type)
values ('15', '104', '2024-02-15', '300.0', 'purchase');
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type)
values ('16', '104', '2024-03-01', '350.0', 'purchase');
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type)
values ('17', '104', '2024-03-10', '280.0', 'purchase');
insert into customer_transactions (transaction_id, customer_id, transaction_date, amount, transaction_type)
values ('18', '104', '2024-03-15', '100.0', 'refund');

select *
from customer_transactions;

select customer_id
from customer_transactions
group by customer_id
having sum(if(transaction_type = 'purchase', 1, 0)) >= 3 and
    datediff(max(transaction_date), min(transaction_date)) >= 30 and
    sum(if(transaction_type = 'refund', 1, 0)) / count(*) < 0.2
order by customer_id;

create database if not exists bookstore;