create database if not exists P3601;
use P3601;

CREATE TABLE drivers (
    driver_id INT,
    driver_name VARCHAR(255)
);
CREATE TABLE trips (
    trip_id INT,
    driver_id INT,
    trip_date DATE,
    distance_km DECIMAL(8, 2),
    fuel_consumed DECIMAL(6, 2)
);
Truncate table drivers;
insert into drivers (driver_id, driver_name)
values ('1', 'Alice Johnson');
insert into drivers (driver_id, driver_name)
values ('2', 'Bob Smith');
insert into drivers (driver_id, driver_name)
values ('3', 'Carol Davis');
insert into drivers (driver_id, driver_name)
values ('4', 'David Wilson');
insert into drivers (driver_id, driver_name)
values ('5', 'Emma Brown');
Truncate table trips;
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed)
values ('1', '1', '2023-02-15', '120.5', '10.2');
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed)
values ('2', '1', '2023-03-20', '200.0', '16.5');
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed)
values ('3', '1', '2023-08-10', '150.0', '11.0');
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed)
values ('4', '1', '2023-09-25', '180.0', '12.5');
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed)
values ('5', '2', '2023-01-10', '100.0', '9.0');
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed)
values ('6', '2', '2023-04-15', '250.0', '22.0');
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed)
values ('7', '2', '2023-10-05', '200.0', '15.0');
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed)
values ('8', '3', '2023-03-12', '80.0', '8.5');
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed)
values ('9', '3', '2023-05-18', '90.0', '9.2');
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed)
values ('10', '4', '2023-07-22', '160.0', '12.8');
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed)
values ('11', '4', '2023-11-30', '140.0', '11.0');
insert into trips (trip_id, driver_id, trip_date, distance_km, fuel_consumed)
values ('12', '5', '2023-02-28', '110.0', '11.5');

select *
from trips;

with t as (select driver_id, if(month(trip_date) <= 6, 0, 1) half_year, avg(distance_km / fuel_consumed) val
           from trips
           group by driver_id, half_year)
select t1.driver_id, d.driver_name, round(t1.val, 2) first_half_avg, round(t2.val, 2) second_half_avg,
    round(t2.val - t1.val, 2) efficiency_improvement
from t t1, t t2, drivers d
where t1.driver_id = t2.driver_id and t1.half_year = 0 and t2.half_year = 1 and t1.driver_id = d.driver_id and
    t2.val - t1.val > 0
order by efficiency_improvement desc, d.driver_name;