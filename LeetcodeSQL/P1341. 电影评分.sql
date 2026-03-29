create database if not exists P1341;
use P1341;

Create table If Not Exists Movies (
    movie_id int,
    title varchar(30)
);
Create table If Not Exists Users (
    user_id int,
    name varchar(30)
);
Create table If Not Exists MovieRating (
    movie_id int,
    user_id int,
    rating int,
    created_at date
);
Truncate table Movies;
insert into Movies (movie_id, title)
values ('1', 'Avengers');
insert into Movies (movie_id, title)
values ('2', 'Frozen 2');
insert into Movies (movie_id, title)
values ('3', 'Joker');
Truncate table Users;
insert into Users (user_id, name)
values ('1', 'Daniel');
insert into Users (user_id, name)
values ('2', 'Monica');
insert into Users (user_id, name)
values ('3', 'Maria');
insert into Users (user_id, name)
values ('4', 'James');
Truncate table MovieRating;
insert into MovieRating (movie_id, user_id, rating, created_at)
values ('1', '1', '3', '2020-01-12');
insert into MovieRating (movie_id, user_id, rating, created_at)
values ('1', '2', '4', '2020-02-11');
insert into MovieRating (movie_id, user_id, rating, created_at)
values ('1', '3', '2', '2020-02-12');
insert into MovieRating (movie_id, user_id, rating, created_at)
values ('1', '4', '1', '2020-01-01');
insert into MovieRating (movie_id, user_id, rating, created_at)
values ('2', '1', '5', '2020-02-17');
insert into MovieRating (movie_id, user_id, rating, created_at)
values ('2', '2', '2', '2020-02-01');
insert into MovieRating (movie_id, user_id, rating, created_at)
values ('2', '3', '2', '2020-03-01');
insert into MovieRating (movie_id, user_id, rating, created_at)
values ('3', '1', '3', '2020-02-22');
insert into MovieRating (movie_id, user_id, rating, created_at)
values ('3', '2', '4', '2020-02-25');


select u.name result
from MovieRating r, Users u
where r.user_id = u.user_id
group by u.name
order by count(rating) desc, name
limit 1;

select movie_id, left(created_at, 7), avg(rating) cnt
from MovieRating
group by movie_id, left(created_at, 7);

select title result
from Movies m, (select movie_id, avg(rating) cnt from MovieRating group by movie_id, left(created_at, 7)) r
where m.movie_id = r.movie_id
order by cnt desc, title
limit 1;

(select u.name results
 from MovieRating r, Users u
 where r.user_id = u.user_id
 group by u.name
 order by count(rating) desc, name
 limit 1)
union all
(SELECT title AS results
 FROM Movies m
          LEFT JOIN MovieRating mr
 ON m.movie_id = mr.movie_id AND YEAR(mr.created_at) = 2020 AND MONTH(mr.created_at) = 2
 GROUP BY mr.movie_id, title
 ORDER BY AVG(mr.rating) DESC, title
 LIMIT 1);

