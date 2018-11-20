# termostato

import mysql.connector
import matplotlib

conn = mysql.connector.connect(
	host='192.168.1.51',
	user='python',
	password='python',
	database='db2017',
)
rs=conn.cursor()
rs.execute("""
	SELECT * FROM temperaturas;
	""")
r=rs.fetchall()

for i in r:	print(i)
