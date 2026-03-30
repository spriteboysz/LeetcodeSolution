create database if not exists P3564;
use P3564;

CREATE TABLE if not exists products (
    product_id INT,
    product_name VARCHAR(255),
    category VARCHAR(50)
);
CREATE TABLE if not exists sales (
    sale_id INT,
    product_id INT,
    sale_date DATE,
    quantity INT,
    price DECIMAL(10, 2)
);
Truncate table sales;
insert into sales (sale_id, product_id, sale_date, quantity, price)
values ('1', '1', '2023-01-15', '5', '10.0');
insert into sales (sale_id, product_id, sale_date, quantity, price)
values ('2', '2', '2023-01-20', '4', '15.0');
insert into sales (sale_id, product_id, sale_date, quantity, price)
values ('3', '3', '2023-03-10', '3', '18.0');
insert into sales (sale_id, product_id, sale_date, quantity, price)
values ('4', '4', '2023-04-05', '1', '20.0');
insert into sales (sale_id, product_id, sale_date, quantity, price)
values ('5', '1', '2023-05-20', '2', '10.0');
insert into sales (sale_id, product_id, sale_date, quantity, price)
values ('6', '2', '2023-06-12', '4', '15.0');
insert into sales (sale_id, product_id, sale_date, quantity, price)
values ('7', '5', '2023-06-15', '5', '12.0');
insert into sales (sale_id, product_id, sale_date, quantity, price)
values ('8', '3', '2023-07-24', '2', '18.0');
insert into sales (sale_id, product_id, sale_date, quantity, price)
values ('9', '4', '2023-08-01', '5', '20.0');
insert into sales (sale_id, product_id, sale_date, quantity, price)
values ('10', '5', '2023-09-03', '3', '12.0');
insert into sales (sale_id, product_id, sale_date, quantity, price)
values ('11', '1', '2023-09-25', '6', '10.0');
insert into sales (sale_id, product_id, sale_date, quantity, price)
values ('12', '2', '2023-11-10', '4', '15.0');
insert into sales (sale_id, product_id, sale_date, quantity, price)
values ('13', '3', '2023-12-05', '6', '18.0');
insert into sales (sale_id, product_id, sale_date, quantity, price)
values ('14', '4', '2023-12-22', '3', '20.0');
insert into sales (sale_id, product_id, sale_date, quantity, price)
values ('15', '5', '2024-02-14', '2', '12.0');
Truncate table products;
insert into products (product_id, product_name, category)
values ('1', 'Warm Jacket', 'Apparel');
insert into products (product_id, product_name, category)
values ('2', 'Designer Jeans', 'Apparel');
insert into products (product_id, product_name, category)
values ('3', 'Cutting Board', 'Kitchen');
insert into products (product_id, product_name, category)
values ('4', 'Smart Speaker', 'Tech');
insert into products (product_id, product_name, category)
values ('5', 'Yoga Mat', 'Fitness');

select (case when floor(month(sale_date) / 3) = 1
                 then 'Spring'
             when floor(month(sale_date) / 3) = 2
                 then 'Summer'
             when floor(month(sale_date) / 3) = 3
                 then 'Fall'
             else 'Winter' end) season, p.category, sum(s.quantity) total_quantity,
    sum(s.quantity * s.price) total_revenue
from sales s
         join products p on s.product_id = p.product_id
group by p.category, season
order by total_quantity desc, total_revenue desc, category;

select *
from (select (case when floor(month(sale_date) / 3) = 1
                       then 'Spring'
                   when floor(month(sale_date) / 3) = 2
                       then 'Summer'
                   when floor(month(sale_date) / 3) = 3
                       then 'Fall'
                   else 'Winter' end) season, p.category, sum(s.quantity) total_quantity,
          sum(s.quantity * s.price) total_revenue
      from sales s
               join products p on s.product_id = p.product_id
      group by p.category, season
      order by total_quantity desc, total_revenue desc, category) t;


WITH CTE AS (SELECT *, ROW_NUMBER() OVER (PARTITION BY season ORDER BY (SELECT 0)) RN
             FROM (select (case when floor(month(sale_date) / 3) = 1
                                    then 'Spring'
                                when floor(month(sale_date) / 3) = 2
                                    then 'Summer'
                                when floor(month(sale_date) / 3) = 3
                                    then 'Fall'
                                else 'Winter' end) season, p.category, sum(s.quantity) total_quantity,
                       sum(s.quantity * s.price) total_revenue
                   from sales s
                            join products p on s.product_id = p.product_id
                   group by p.category, season
                   order by total_quantity desc, total_revenue desc, category) t)
SELECT season, category, total_quantity, total_revenue
FROM CTE
WHERE RN = 1
order by season;
