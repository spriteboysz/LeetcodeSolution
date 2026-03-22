create database if not exists P1795;
use P1795;

Create table If Not Exists Products (
    product_id int,
    store1 int,
    store2 int,
    store3 int
);
Truncate table Products;
insert into Products (product_id, store1, store2, store3)
values ('0', '95', '100', '105');
insert into Products (product_id, store1, store2, store3)
values ('1', '70', NULL, '80');

select *
from Products;

SELECT product_id, 'store1' store, store1 price
FROM Products
WHERE store1 IS NOT NULL
union
select product_id, 'store2' store, store2 price
from Products
where store2 is not null
union
select product_id, 'store3' store, store3 price
from Products
where store3 is not null;

