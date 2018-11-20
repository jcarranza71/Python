r# termostato

import mysql.connector
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

conn = mysql.connector.connect(
	host='localhost',
	user='root',
	password='',
	database='db2017',
)
rs=conn.cursor()
rs.execute("""
	SELECT temperatura FROM temperaturas;
	""")
r=rs.fetchall()

#for i in r:	print(i)

# Data for plotting
#t = np.arange(0.0, 2.0, 0.01)
#s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(r)

ax.set(xlabel='muestras', ylabel='Tª (ºC)',
       title='Registro de temperaturas')
ax.grid()

fig.savefig("test.png")
plt.show()