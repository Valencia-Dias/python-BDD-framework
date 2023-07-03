import mysql.connector
import datetime
from utilities.configurations import *

# 4 parameters- host, db, user, pass
# 1. to establish the connection
# conn = mysql.connector.connect(host="localhost", database="APIDevelop", user="root", password="password")

conn = getConnection()
print(conn.is_connected())

# 2. to send the queries and get the results
# cursor is like   a streamline between the db and python through the connection object
# buffered= True-> to avoid lazy loading
cursor = conn.cursor(buffered=True)
cursor.execute("select * from CustomerInfo")

# 3. fetch the results
# fetchall- fetches all the rows of a table- returns a list of tuples
# fetchone-returns the first row -returns a tuple
# row1 = cursor.fetchone()
# print(row1)
rows = cursor.fetchall()
print(rows)
# If the cursor is on row 1 and u do fetch one first and than do fetch all it will fetch the remaining and not the frist one
sum = 0
for row in rows:
    # sum = sum + row[2]
    sum += row[2]
print("Sum is " + str(sum))

# update the query but using python
# update customerInfo set Location = 'US' where CourseName = 'Jmeter';
query = "update CustomerInfo set Location = %s where CourseName = %s"
data = ("UK", "Jmeter")
cursor.execute(query, data)
conn.commit()

# cursor.execute("select * from CustomerInfo")  # this is just to cehck if the update has happened or not

# data1 = ('Appium',)
# cursor.execute('delete from CustomerInfo where CourseName = %s', data1)
# conn.commit()
# cursor.execute("select * from CustomerInfo")  # this is just to cehck if the update has happened or not

# Insert
# cursor.execute("SELECT CURDATE()")
# data2 = ["Jmeter", '2020-05-12', 345, "India"]
# cursor.execute("Insert into CustomerInfo (CourseName,PurchasedDate,Amount,Location) values (%s, %s,%s,%s)", data2)
# conn.commit()

cursor.execute("select * from CustomerInfo")  # this is just to cehck if the update has happened or not

conn.close()
