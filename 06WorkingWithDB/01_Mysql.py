import os
import cx_Oracle
import csv
 
SQL="SELECT * FROM emp"
 
# Network drive somewhere
filename="E:\Python\WorkingWithDB\Output.csv"
FILE=open(filename,"w");
output=csv.writer(FILE, dialect='excel')
 
# You can set these in system variables but just in case you didnt
os.putenv('ORACLE_HOME', 'E:\app\brije\product\11.2.0\dbhome_1') 
os.putenv('LD_LIBRARY_PATH', 'E:\app\brije\product\11.2.0\dbhome_1\lib') 
 
#connection = cx_Oracle.connect('userid/password@99.999.9.99:PORT/SID')
connection = cx_Oracle.connect('system/system@localhost:1521/orahome')
 
cursor = connection.cursor()
cursor.execute(SQL)
for row in cursor:
    output.writerow(row)
cursor.close()
connection.close()
FILE.close()
