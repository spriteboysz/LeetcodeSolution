create database if not exists P1045;
use P1045;

Create table If Not Exists Customer (
    customer_id int,
    product_key int
);
Create table Product (
    product_key int
);
Truncate table Customer;
insert into Customer (customer_id, product_key)
values ('1', '5');
insert into Customer (customer_id, product_key)
values ('2', '6');
insert into Customer (customer_id, product_key)
values ('3', '5');
insert into Customer (customer_id, product_key)
values ('3', '6');
insert into Customer (customer_id, product_key)
values ('1', '6');
Truncate table Product;
insert into Product (product_key)
values ('5');
insert into Product (product_key)
values ('6');

select *
from Customer;

-- 报告 Customer 表中购买了 Product 表中所有产品的客户的 id
select customer_id
from Customer
group by customer_id
having count(distinct product_key) = (select count(product_key) from Product);
