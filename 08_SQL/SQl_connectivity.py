# Step 1: Install and import mysql-connector-python
# mysql-connector-python is a Python library to connect and interact with MySQL databases.
import mysql.connector as con

# Step 2: Create a connection object to connect to the MySQL server
# The `connect` method is used to establish a connection to the MySQL database.
mysql = con.connect(
    host="localhost",      # MySQL server host (usually "localhost" for local development)
    user="root",           # MySQL username
    password="root",       # MySQL password
    database="sql_con_py"  # The name of the database to connect to (optional for initial connection)
    # database="ecommerce"  
)

# Check if the connection was successful
if mysql.is_connected():
    print("Connected to MySQL")

# Step 3: Create a Cursor object
# A cursor is a control structure that enables interaction with the database, allowing you to execute queries and fetch results.
cur = mysql.cursor()

# Step 4: Create a new database (uncomment if needed)
# execute(): The `execute` method runs SQL queries on the connected database.

# cur.execute("CREATE DATABASE sql_con_py")  # Uncomment this line to create the database if it doesn't exist.

# Step 5: Retrieve all databases
# The `SHOW DATABASES` query retrieves a list of all databases in the MySQL server.
# cur.execute("SHOW DATABASES")  # Executes the query to show all databases

# Fetch all results from the executed query
# `fetchall()` retrieves all rows of the query result as a list of tuples.
# result_all = cur.fetchall()
# print("----------- All Databases ------------")
# print(result_all)

# Step 6: Fetch one record
# `fetchone()` fetches the next row of a query result set, returning it as a single tuple.
# result_one = cur.fetchone()  # Fetches the next record from the result set (if available)
# print("----------- Single Record ------------")
# print(result_one)

# Step 7: Fetch multiple records
# `fetchmany(size)` retrieves the specified number of rows (size) as a list of tuples.
# result_many = cur.fetchmany(size=1)  # Fetches the next 2 records from the result set
# print("------------- Multiple Records ----------------")
# print(result_many)

# Step 8: Get the number of rows affected by the query
# `rowcount` returns the number of rows affected by the last executed query.
# print("-------------- Number of rows returned --------")
# print(cur.rowcount)
                     

# Fetch data from exitsing database
# cur.execute("SELECT * FROM Customers")
# result = cur.fetchall()
# print("Data from Customers table:")
# for row in result:
#     print(row)

# Step 9: Perform operations and execute additional queries
# Example of creating a table (if it doesn't already exist)
# cur.execute("""
# CREATE TABLE IF NOT EXISTS students (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100),
#     age INT,
#     grade VARCHAR(5)
# )
# """)

# Insert a record into the table (use prepared statements for safety)
# cur.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ("John Doe", 20, "A"))
# mysql.commit()  # Commit the changes to make them permanent

# Retrieve records from the table
# cur.execute("SELECT * FROM students")
# records = cur.fetchall()
# print("Students Table Records:")
# for record in records:
#     print(record)

# Step 10: Close the cursor and connection
# Always close the cursor and the connection to release resources.
cur.close()
mysql.close()
print("MySQL connection closed.")
