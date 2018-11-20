# db: mysql
import pip
pip.main(['install','mysql-connector-python-rf'])
#import mysql.connector
from mysql.connector import (connection)
#conn=mysql.connector.connect(
conn=connection.MySQLConnection(
	host='52.47.137.67',
	user='santander1',
	password='santander1',
	database='dblancoformacion'
	)
rs=conn.cursor()
rs.execute('''
	SELECT * FROM eoi;
	''')
r=rs.fethcall()
for i in r:
	print(r)
conn.close()