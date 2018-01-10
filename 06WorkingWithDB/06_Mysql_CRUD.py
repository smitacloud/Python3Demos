#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","root","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

'''To perform CRUD operation make sure you have installed MYSQLdb pacakge in your Python.

Like anyother programing language Python also need below step to perform CRUD on Database.

1-Import required API module for us as the data base is MYSQL we should import MYSQLdb in our Python file.

2- Acquiring connection with the database.

3- Performing SQL statments

4:- Closing the connection

 '''
#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","root","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query 
cursor.execute("SELECT VERSION()")

# Fetch a single row 
data = cursor.fetchone()

print ("Database version : %s " % data)

# Drop table if it already exist 
cursor.execute("DROP TABLE IF EXISTS SMITA_TEST")

# Create table Example
sql = "CREATE TABLE SMITA_TEST (FNAME CHAR(20) NOT NULL,LNAME CHAR(20),AGE INT, GENDER CHAR(1),INCOME FLOAT )"

cursor.execute(sql)

# Inserting in Table Example:- Prepare SQL query to INSERT a record into the database and accept the value dynamic. This is similar to prepare statement which we create.
sql = "INSERT INTO SMITA_TEST(FNAME, \
LNAME, AGE, GENDER, INCOME) \
VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
('Smita', 'Kumar', 35, 'F', 2000)
try:
   # Execute command
   cursor.execute(sql)
   # Commit changes
   db.commit()
except:
   # Rollback if needed
   db.rollback()
   # disconnect from server

# Select Query Example :- Selecting data from the table.
sql = "SELECT * FROM SMITA_TEST"
#\
#WHERE AGE > ‘%d'" % (35)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      gender = row[3]
      income = row[4]
      # Now print fetched result
      print ("fname=%s,lname=%s,age=%d,gender=%s,income=%d" % (fname, lname, age, gender, income ))
      print ("New fname=,lname=,age=,gender=,income=" % (fname, lname, age, gender, income ))
except:
   print ("Value Fetch properly")

# Update Exmaple:- Update record 
sql = "UPDATE SMITA_TEST SET INCOME = 5000 WHERE GENDER = '%c'" % ('M')
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# Delete Operation :- Delete Opearations
sql = "DELETE FROM SIDDHU_TEST WHERE INCOME = '%d'" % (5000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

db.close()
