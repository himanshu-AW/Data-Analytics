CREATE database ecommerce;

USE ecommerce;

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Email VARCHAR(255),
    City VARCHAR(255),
    Country VARCHAR(255)
);


INSERT INTO Customers (CustomerID, FirstName, LastName, Email, City, Country) VALUES
(101, 'John', 'Doe', 'john.doe@example.com', 'New York', 'USA'),
(102, 'Jane', 'Smith', 'jane.smith@example.com', 'London', 'UK'),
(103, 'Michael', 'Brown', 'michael.brown@example.com', 'Sydney', 'Australia'),
(104, 'Emily', 'Davis', 'emily.davis@example.com', 'Toronto', 'Canada'),
(105, 'Daniel', 'Wilson', 'daniel.wilson@example.com', 'Miami', 'USA'),
(106, 'Sarah', 'Taylor', 'sarah.taylor@example.com', 'San Francisco', 'USA'),
(107, 'James', 'Anderson', 'james.anderson@example.com', 'Berlin', 'Germany'),
(108, 'Sophia', 'Moore', 'sophia.moore@example.com', 'Paris', 'France'),
(109, 'Olivia', 'Thomas', 'olivia.thomas@example.com', 'Rome', 'Italy'),
(110, 'Liam', 'Jackson', 'liam.jackson@example.com', 'Tokyo', 'Japan'),
(111, 'Emma', 'Martin', 'emma.martin@example.com', 'Madrid', 'Spain');


CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES
(1, 101, '2023-01-15', 250.50),
(2, 102, '2023-01-20', 150.00),
(3, 103, '2023-02-05', 320.75),
(4, 104, '2023-02-10', 980.00),
(5, 105, '2023-03-08', 1125.00),
(6, 101, '2023-03-15', 300.00),
(7, 102, '2023-04-01', 450.25),
(8, 106, '2023-05-12', 760.00),
(9, 107, '2023-06-20', 540.50),
(10, 108, '2023-07-15', 1250.00),
(11, 103, '2023-08-01', 675.50),
(12, 109, '2023-08-20', 890.00),
(13, 110, '2023-09-12', 990.00),
(14, 104, '2023-10-03', 400.00),
(15, 111, '2023-11-22', 1340.00);


CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    Category VARCHAR(255),
    Price DECIMAL(10, 2)
);

INSERT INTO Products (ProductID, ProductName, Category, Price) VALUES
(201, 'Laptop', 'Electronics', 1000.00),
(202, 'Smartphone', 'Electronics', 700.00),
(203, 'Tablet', 'Electronics', 500.00),
(204, 'Headphones', 'Accessories', 100.00),
(205, 'Keyboard', 'Accessories', 50.00),
(206, 'Mouse', 'Accessories', 30.00),
(207, 'Chair', 'Furniture', 200.00),
(208, 'Desk', 'Furniture', 300.00),
(209, 'Monitor', 'Electronics', 250.00),
(210, 'Printer', 'Electronics', 150.00);


CREATE TABLE Order_Items (
    OrderItemID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

INSERT INTO Order_Items (OrderItemID, OrderID, ProductID, Quantity) VALUES
(301, 1, 201, 1), 
(302, 2, 202, 2),
(303, 3, 203, 1), 
(304, 4, 204, 5),
(305, 5, 205, 10),
(306, 6, 206, 3), 
(307, 7, 207, 2), 
(308, 8, 208, 1),
(309, 9, 209, 1), 
(310, 10, 210, 4),
(312, 12, 202, 3),
(313, 13, 203, 2), 
(314, 14, 204, 3), 
(315, 15, 205, 1);

-- Question 1:  
SELECT COUNT(o.OrderID) AS TotalOrders
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE c.Country = 'USA';

-- Question 2:
SELECT DISTINCT c.FirstName, c.LastName
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE o.TotalAmount > 1000;

-- Question 3: 
SELECT p.ProductName, SUM(oi.Quantity) AS TotalQuantitySold
FROM Products p
JOIN Order_Items oi ON p.ProductID = oi.ProductID
GROUP BY p.ProductName
ORDER BY TotalQuantitySold DESC
LIMIT 5;

-- Question 4:
SELECT p.Category, SUM(oi.Quantity * p.Price) AS TotalRevenue
FROM Products p
JOIN Order_Items oi ON p.ProductID = oi.ProductID
GROUP BY p.Category;

-- Question 5:
SELECT c.FirstName, c.LastName
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE o.OrderID IS NULL;

-- Question 6:
SELECT c.Country, AVG(o.TotalAmount) AS AverageOrderAmount
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.Country;

-- Question 7:
SELECT MONTH(o.OrderDate) AS Month, COUNT(o.OrderID) AS TotalOrders
FROM Orders o
WHERE YEAR(o.OrderDate) = 2023
GROUP BY MONTH(o.OrderDate)
ORDER BY Month;

-- Question 8:
SELECT p.ProductName
FROM Products p
LEFT JOIN Order_Items oi ON p.ProductID = oi.ProductID
WHERE oi.OrderItemID IS NULL;


SELECT c.FirstName, c.LastName, COUNT(o.OrderID) AS TotalOrders
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.FirstName, c.LastName
ORDER BY TotalOrders DESC
LIMIT 1;


