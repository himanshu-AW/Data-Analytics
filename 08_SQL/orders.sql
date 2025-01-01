select * from orders;

SELECT STR_TO_DATE(orderDate, '%d-%m-%Y') AS orderDate2 from orders;

-- convert text-date to date format
SET SQL_SAFE_UPDATES = 0;

UPDATE orders SET orderDate = STR_TO_DATE(orderDate,'%d-%m-%Y');
UPDATE orders SET requiredDate = STR_TO_DATE(requiredDate,'%d-%m-%Y');
UPDATE orders SET shippedDate = STR_TO_DATE(shippedDate,'%d-%m-%Y');

select * from orders;

select date(orderDate) as dates from orders;
select time(orderDate) as dates from orders;
select datediff(shippedDate,orderDate) as dates from orders;

select day(orderDate) as Days from orders;
select dayname(orderDate) as DaysName from orders;
select month(orderDate) as Months from orders;
select monthname(orderDate) as MonthsName from orders;
select year(orderDate) as Years from orders;
select yearweek(orderDate) as YearWeeks from orders;




