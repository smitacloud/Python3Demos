

'''
MySQL CRUD (Create Retrieve Update Delete) Operations using Python
'''
__author__ = "Smita B Kumar"

__license__ = "Synergetics"
__version__ = "0.0.1"
__email__ = "brijeshsmita@gmail.com"
__status__ = "Training/Development"

#!/usr/bin/python3
# pip install pymysql
# pip install mysqlclient
import pymysql as mdb
import sys
import pymysql



# CREATE A NEW TABLE and INSERT SOME VALUES
def createTable(con):
    with con:

        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS TableTest")
        cur.execute("CREATE TABLE TableTest(Id INT PRIMARY KEY AUTO_INCREMENT, \
                     Name VARCHAR(25))")
        cur.execute("INSERT INTO TableTest(Name) VALUES('Babbo Natale')")
        cur.execute("INSERT INTO TableTest(Name) VALUES('Tizio')")
        cur.execute("INSERT INTO TableTest(Name) VALUES('Caio')")
        cur.execute("INSERT INTO TableTest(Name) VALUES('Sempronio')")
        cur.execute("INSERT INTO TableTest(Name) VALUES('Giulio Cesare')")



# RETRIEVE TABLE ROWS
def retrieveTable(con):
    with con:

        cur = con.cursor()
        cur.execute("SELECT * FROM TableTest")

        results = cur.fetchall()

        for row in results:
            id = row[0]
            name = row[1]
            print ("id=%d,name=%s" % (id, name))



# UPDATE ROW
def updateRow(con):
    with con:

        cur = con.cursor()

        cur.execute("UPDATE TableTest SET Name = %s WHERE Id = %s",
            ("Nome Acaso", "4"))

        print("Number of rows updated:",  cur.rowcount)



# DELETE ROW
def deleteRow(con):
    with con:

        cur = con.cursor()

        cur.execute("DELETE FROM TableTest WHERE Id = %s", "2")

        print("Number of rows deleted:", cur.rowcount)



# SET UP THE CONNECTION
try:
   # Open database connection
   con = mdb.connect("localhost","root","root","TESTDB" );
    
   # prepare a cursor object using cursor() method
   cur = con.cursor()
   cur.execute("SELECT VERSION()")

   ver = cur.fetchone()

   print("Database version : %s " % ver)


   # CRUD OPERATIONS
   createTable(con)
   retrieveTable(con)
   updateRow(con)
   deleteRow(con)


except mdb.Error as e:
    print("Error %d: %s" % (e.args[0],e.args[1]))
    sys.exit(1)


finally:

    if con:
        con.close()

