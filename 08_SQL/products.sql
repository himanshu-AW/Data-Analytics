-- Use the RENAME TABLE statement:
RENAME TABLE payment to products;

select * from products;

-- Case is used when we need to apply conditions like (if-else) then we use it.

select productName,quantityInStock, 
	case 
		when quantityInStock < 1000 then "URGENT NEED OF STOCKS"
		else "enough stocks"
	end as requirementOfStocks
from products;

-- group by
select productLine,count(productCode) from products group by productLine;
select productLine,count(productCode) from products group by productLine order by count(productCode) desc;

-- having clause 
select  productLine, count(productCode) from products group by productLine having count(productCode) >= 20;
select productLine,sum(quantityInStock),sum(buyPrice) from products group by productLine having sum(quantityInStock) > 20000;

-- joins (inner,left,right,outer)
-- Inner join : Return common rows from both the tables(products,orderdetails)
select * from products as pd
inner join orderdetails as od
on pd.productCode = od.productCode;

select pd.productName,sum(od.quantityOrdered) 
from products as pd
inner join orderdetails as od
on pd.productCode = od.productCode
group by pd.productName;


-- left join: return all rows from left table and also return matching rows from right table
select pd.productName,od.quantityOrdered
from products as pd
left join orderdetails as od
on pd.productCode = od.productCode; 

-- right join: return all rows from right table and also return matching rows from left table
select pd.productName,od.quantityOrdered
from products as pd
right join orderdetails as od
on pd.productCode = od.productCode; 

-- cross join: return all rows from left table and right table as well.
select pd.productName,od.quantityOrdered
from products as pd
cross join orderdetails as od
on pd.productCode = od.productCode;

