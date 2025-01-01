select * from orderdetails;
describe orderdetails;

SELECT productCode, quantityOrdered,
  CASE 
    WHEN quantityOrdered >= 40 THEN 'Higher order'
    WHEN quantityOrdered < 30 THEN 'Low order'
    ELSE 'Average order'
  END AS orderCategory
FROM orderdetails;