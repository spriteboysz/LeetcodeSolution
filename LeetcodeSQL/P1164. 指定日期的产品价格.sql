create database if not exists P1164;
use P1164;

Create table If Not Exists Products (
    product_id int,
    new_price int,
    change_date date
);
Truncate table Products;
insert into Products (product_id, new_price, change_date)
values ('1', '20', '2019-08-14');
insert into Products (product_id, new_price, change_date)
values ('2', '50', '2019-08-14');
insert into Products (product_id, new_price, change_date)
values ('1', '30', '2019-08-15');
insert into Products (product_id, new_price, change_date)
values ('1', '35', '2019-08-16');
insert into Products (product_id, new_price, change_date)
values ('2', '65', '2019-08-17');
insert into Products (product_id, new_price, change_date)
values ('3', '20', '2019-08-18');

select *
from Products;

select product_id, max(change_date)
from Products
where datediff('2019-08-16', change_date) >= 0
group by product_id;

select product_id, new_price price
from Products
where (product_id, change_date) in (select product_id, max(change_date)
                                    from Products
                                    where datediff('2019-08-16', change_date) >= 0
                                    group by product_id);


select distinct p.product_id, ifnull(t.new_price, 10) as price
from Products p
         left join (select product_id, new_price
                    from Products
                    where (product_id, change_date) in (select product_id, max(change_date)
                                                        from Products
                                                        where datediff('2019-08-16', change_date) >= 0
                                                        group by product_id)) t on p.product_id = t.product_id;