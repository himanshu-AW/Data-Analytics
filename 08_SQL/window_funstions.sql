create database window_session;
use window_session;
create table student(s_name varchar(30),s_score int);
insert into student values("Aryan",200),("Ram",200),("Aman",200),
("Aryan",300),("Aman",300),("Shyam",300),("Aryan",400),("Ram",400),("Aman",400),("Shyam",400),
("Ram",500),("Shyam",500);
select * from student;

-- window function appliyes aggregate,ranking and analytic function over a particular window(set of rows) 
-- Over() caluse :-used with to defined that window
-- * aggregate fun() :- give o/p one row per execution
-- * window fun() : the row maintaned thrie seperate identities.

-- ranking fun() - rank, row_rank,dense_rank,percent_rank
-- analytic/value - lead.leg,first_value,last_value 


-- -------------Window function ------------
SELECT s_name,s_score,
SUM(s_score) OVER(partition by s_name ORDER BY s_score ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS TotalScore
FROM student; 

SELECT s_name,s_score,
SUM(s_score) OVER(partition by s_name ORDER BY s_score) AS TotalScore,
AVG(s_score) OVER(partition by s_name ORDER BY s_score) AS AverageScore,
COUNT(s_score) OVER(partition by s_name ORDER BY s_name) AS CountScore,
MIN(s_score) OVER (partition by s_name order by s_score) As MinScore,
MAX(s_score) OVER (partition by s_name order by s_score) as MaxScore
FROM student; 

SELECT s_name,s_score,
ROW_NUMBER() OVER(ORDER BY s_score) as Student_RowNo,
RANK() OVER(ORDER BY s_score) as Rank_Student,
dense_rank() over(order by s_score) as dense_ranking,
percent_rank() over(order by s_score) as percent_ranking
FROM student; 

--  Partition by divides the row into partions so w can specify "which rows to use to comple the window function"
-- order by is use to show that, we can order by rows within partitions (this is optional and does not need tp spacify)
-- Rows : it can be used if we want further limit the rows with in our partition (optional)

SELECT s_name,s_score,
first_value(s_name) OVER(ORDER BY s_score) AS firstValue,
last_value(s_name) OVER(ORDER BY s_score) AS LastValue,
LEAD(s_score) OVER(ORDER BY s_score) AS leadValue,
LAG(s_score) OVER(ORDER BY s_score) AS lagValue
FROM student; 
