create database if not exists P3626;
use P3626;

CREATE TABLE if not exists stores (
    store_id INT,
    store_name VARCHAR(255),
    location VARCHAR(255)
);
CREATE TABLE if not exists inventory (
    inventory_id INT,
    store_id INT,
    product_name VARCHAR(255),
    quantity INT,
    price DECIMAL(10, 2)
);
Truncate table stores;
insert into stores (store_id, store_name, location)
values ('1', 'Downtown Tech', 'New York');
insert into stores (store_id, store_name, location)
values ('2', 'Suburb Mall', 'Chicago');
insert into stores (store_id, store_name, location)
values ('3', 'City Center', 'Los Angeles');
insert into stores (store_id, store_name, location)
values ('4', 'Corner Shop', 'Miami');
insert into stores (store_id, store_name, location)
values ('5', 'Plaza Store', 'Seattle');
Truncate table inventory;
insert into inventory (inventory_id, store_id, product_name, quantity, price)
values ('1', '1', 'Laptop', '5', '999.99');
insert into inventory (inventory_id, store_id, product_name, quantity, price)
values ('2', '1', 'Mouse', '50', '19.99');
insert into inventory (inventory_id, store_id, product_name, quantity, price)
values ('3', '1', 'Keyboard', '25', '79.99');
insert into inventory (inventory_id, store_id, product_name, quantity, price)
values ('4', '1', 'Monitor', '15', '299.99');
insert into inventory (inventory_id, store_id, product_name, quantity, price)
values ('5', '2', 'Phone', '3', '699.99');
insert into inventory (inventory_id, store_id, product_name, quantity, price)
values ('6', '2', 'Charger', '100', '25.99');
insert into inventory (inventory_id, store_id, product_name, quantity, price)
values ('7', '2', 'Case', '75', '15.99');
insert into inventory (inventory_id, store_id, product_name, quantity, price)
values ('8', '2', 'Headphones', '20', '149.99');
insert into inventory (inventory_id, store_id, product_name, quantity, price)
values ('9', '3', 'Tablet', '2', '499.99');
insert into inventory (inventory_id, store_id, product_name, quantity, price)
values ('10', '3', 'Stylus', '80', '29.99');
insert into inventory (inventory_id, store_id, product_name, quantity, price)
values ('11', '3', 'Cover', '60', '39.99');
insert into inventory (inventory_id, store_id, product_name, quantity, price)
values ('12', '4', 'Watch', '10', '299.99');
insert into inventory (inventory_id, store_id, product_name, quantity, price)
values ('13', '4', 'Band', '25', '49.99');
insert into inventory (inventory_id, store_id, product_name, quantity, price)
values ('14', '5', 'Camera', '8', '599.99');
insert into inventory (inventory_id, store_id, product_name, quantity, price)
values ('15', '5', 'Lens', '12', '199.99');

select *
from inventory;

select store_id, product_name, quantity, price
from inventory
where store_id = 1
order by price desc, quantity desc
limit 1;

select store_id
from inventory;

select distinct store_id,
    first_value(product_name) over (partition by store_id order by price desc, quantity desc) as name
from inventory;

select distinct store_id, first_value(product_name) over (partition by store_id order by price, quantity) as name
from inventory;

select t1.store_id, t1.name, i.quantity, i.price
from (select distinct store_id,
          first_value(product_name) over (partition by store_id order by price desc, quantity desc) as name
      from inventory) t1
         left join inventory i on t1.store_id = i.store_id and t1.name = i.product_name;

select t2.store_id, t2.name, i.quantity, i.price
from (select distinct store_id,
          first_value(product_name) over (partition by store_id order by price, quantity) as name
      from inventory) t2
         left join inventory i on t2.store_id = i.store_id and t2.name = i.product_name;


