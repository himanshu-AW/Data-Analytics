-- SHOW DATABASES;
-- USE rd;

-- SELECT * FROM esd;
-- SELECT JobTitle,FullName,AnnualSalary FROM esd WHERE JobTitle = "Sr. Manger";

-- describe esd;


-- INSERT INTO esd VALUES('e0100',"Charly","CEO","IT","R&D","Male","Asian",22,"08-08-2002","$1,000,000","50%","INDIA","Muradnagar","");
-- Select * From esd Where EEID = 'e0100';

-- INSERT INTO esd(FullName,EEID,JobTitle,Department,Gender,Country,Age,HireDate,AnnualSalary,Bonus,City) 
-- VALUES("Ap Singh",'e0101',"HOD","IT","Male", "INDIA",24,"08-08-2000","$10,000","5%","Dlhi");
-- Select * From esd Where EEID = 'e0101';

-- select * from esd where City = "Seattle";
-- select JobTitle,FullName,AnnualSalary from esd where JobTitle = "Sr. Manger";
-- select FullName,AnnualSalary,JobTitle,City from esd where JobTitle = "Sr. Manger" and City= "Seattle";
-- select FullName,AnnualSalary,JobTitle,Country from esd where JobTitle = "Sr. Manger" and Country= "China";
-- select FullName,AnnualSalary,JobTitle,Gender from esd where not Gender= "Male";

-- Select * from esd where FullName like "mar%";
-- Select * from esd where FullName like "%mar";
-- Select * from esd where FullName like "%mar%";


-- select * from esd order by Department asc;
-- select * from esd order by Department asc,Age desc;
-- select * from esd order by Department,Age asc;


-- select * from esd order by Age asc limit 5;
-- select * from esd limit 5;

-- between from_start and to_end
select * from esd where AnnualSalary between '$1,30,000' and '$1,50,000' order by AnnualSalary asc;


-- in & not in 
select * from esd where Department in ('IT');
select * from esd where Department in ('IT','Accounting');
select * from esd where Department not in ('IT','Accounting');

select * from esd where Department in ('IT','Accounting') and City in ('Miami','Seattle');


-- ------- STRING functions ---------
-- concat() : to combine two or more columns
select concat(JobTitle," - ",Department) as Designation from esd;
select concat(FullName," - ",JobTitle," - ",Department) as Emp_Details from esd;

-- concat_ws() - instead of adding delimeter between two columns many times. we can only pass a delimeter for one time and does not matter how many columns you passes for combining.
select concat_ws(" - ",JobTitle,Department) as Designation from esd;   
select concat_ws(" - ",FullName,JobTitle,Department) as Emp_Details from esd;
select concat_ws(" - ",FullName,JobTitle,Department,Gender) as Emp_Details from esd;

-- length() to find length of string
select length(FullName) as Name_length from esd;

-- Upper() : to convert a string into uppercase string
select Upper(FullName) as Names from esd;

-- Lower() : to convert a string into lowercase string
select Lower(FullName) as Names from esd;


-- left() to find the first n characters from a given string
select left(FullName,4) as Username from esd;
select left(FullName,1) as Username from esd;

-- right() to find the last n characters from a given string
select right(FullName,4) as Username from esd;
select right(FullName,1) as Username from esd;

-- mid() to find the some characters like first param:start and 2nd param:number of characters
select mid(FullName,2,5) as midname from esd;
select mid(FullName,1) as midname from esd;

-- Group by : to categorize the data based on specific columns. like categorize our data based On Country
select Country, count(EEID) as NoOfEmployee from esd Group by Country;
select Department, count(EEID) as NoOfEmployee from esd Group by Department;
select Gender, count(EEID) as NoOfEmployee from esd Group by Gender;

