create database if not exists P1084;
use P1084;

Create table If Not Exists Product (
    product_id int,
    product_name varchar(10),
    unit_price int
);
Create table If Not Exists Sales (
    seller_id int,
    product_id int,
    buyer_id int,
    sale_date date,
    quantity int,
    price int
);
Truncate table Product;
insert into Product (product_id, product_name, unit_price)
values ('1', 'S8', '1000');
insert into Product (product_id, product_name, unit_price)
values ('2', 'G4', '800');
insert into Product (product_id, product_name, unit_price)
values ('3', 'iPhone', '1400');
Truncate table Sales;
insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price)
values ('1', '1', '1', '2019-01-21', '2', '2000');
insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price)
values ('1', '2', '2', '2019-02-17', '1', '800');
insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price)
values ('2', '2', '3', '2019-06-02', '1', '800');
insert into Sales (seller_id, product_id, buyer_id, sale_date, quantity, price)
values ('3', '3', '4', '2019-05-13', '2', '2800');

-- 报告 2019年春季 才售出的产品。即 仅 在 2019-01-01 （含）至 2019-03-31 （含）之间出售的商品
select p.product_id, p.product_name
from Product p
         join Sales s on p.product_id = s.product_id
where s.sale_date not between '2019-01-01' and '2019-03-31';

select product_id, product_name
from Product
where product_id in (select product_id from Sales) and
    product_id not in (select p.product_id
                       from Product p
                                join Sales s on p.product_id = s.product_id
                       where s.sale_date not between '2019-01-01' and '2019-03-31');