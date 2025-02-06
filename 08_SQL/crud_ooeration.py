import mysql.connector as mysql_con

con = mysql_con.connect(
    host="localhost",
    user="root",
    password="root",
    database="sedi"
)

#Check connection is connected or not.
if con.is_connected():
    print("Connected to MySQL!")

#Create a cursor object
cur = con.cursor()

#Create database
#create_db = "CREATE DATABASE IF NOT EXISTS SEDI"
#cur.execute(create_db)
#print("DataBase Successfully Created.")

#Fetch all databases
#show_dbs=cur.fetchall()
#print(show_dbs)

#create_table = "CREATE TABLE student(sid int,sname varchar(20),smarks float)"
#cur.execute(create_table)
#print("Student table created successflly!")

#Insert Data By user input

'''
while True :
    sid = int(input("Enter student id: "))
    sname= input("Enter Student Name: ")
    smarks = float(input("Enter Marks: "))

    input_data = "INSERT INTO student VALUES ({},'{}',{})".format(sid,sname,smarks)
    cur.execute(input_data)
    con.commit()
    print("Data added successfully!\n")

    print("Do you want to add more data? (Press y for Yes)")
    ch = input()
    if 'y' != ch.lower():
        break;
'''
 

#Fetch data from student table
'''
cur.execute("SELECT * FROM student")
result_data = cur.fetchall()
print("--------- Student data --------")
for row in result_data:
    print(f"Student id: {row[0]}")
    print(f"Student Name: {row[1]}")
    print(f"Student Marks: {row[2]}")
'''

def fetchdata():
    cur.execute("SELECT * FROM student")
    result_data = cur.fetchall()
    print("--------- Student data --------")
    for row in result_data:
        print(row)

#Update in existing table/data

fetchdata()

new_name = input("Enter new name: ")
updated_data = f"UPDATE student SET sname = '{new_name}' WHERE sid = 101"
cur.execute(updated_data)
con.commit()

fetchdata()


    





