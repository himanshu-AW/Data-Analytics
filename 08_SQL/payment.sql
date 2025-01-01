-- Aggregation functions : works on numeric data
select * from payments;
select sum(amount) as total_amount from payments;
select count(amount) as no_of_payment from payments;
select max(amount) as max_amount from payments ;
select Min(amount) as min_amount from payments ;
select truncate(amount,0) as amount from payments;
select ceil(amount) as amount_upper_value from payments;
select floor(amount) as amount_upper_value from payments;

