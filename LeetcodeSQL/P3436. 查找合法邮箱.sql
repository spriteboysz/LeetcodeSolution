create database if not exists P3436;
use P3436;

CREATE TABLE If not Exists Users (
    user_id INT,
    email VARCHAR(255)
);
Truncate table Users;
insert into Users (user_id, email)
values ('1', 'alice@example.com');
insert into Users (user_id, email)
values ('2', 'bob_at_example.com');
insert into Users (user_id, email)
values ('3', 'charlie@example.net');
insert into Users (user_id, email)
values ('4', 'david@domain.com');
insert into Users (user_id, email)
values ('5', 'eve@invalid');

select user_id, email
from Users
where regexp_like(email, '^[A-Za-z0-9_]+@[A-Za-z]+\\.com$')
order by user_id;