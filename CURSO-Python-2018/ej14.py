# pesca

import mysql.connector
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
		host='localhost',
		user='root',
		password='',
		database='eoi',
	)
rs=conn.cursor()
rs.execute(
	'''
SELECT DISTINCT A3_ESP_CAT FROM pesca WHERE
  RESPONSABLE_MUESTREO='ESTHER MÉNDEZ FERNÁNDEZ';
	'''
	)
r=rs.fetchall()

especies=[]
for i in r:
	especies.append(i[0])
tallas=[]
for i in especies:
	tallas_i=[]
	rs.execute(
'''
SELECT TALLA FROM pesca WHERE
  RESPONSABLE_MUESTREO='ESTHER MÉNDEZ FERNÁNDEZ'
  AND A3_ESP_CAT="'''+i+'''";
'''
		)
	r=rs.fetchall()
	for j in r:
		tallas_i.append(float(j[0]))
	tallas.append(tallas_i)

fig1, ax1 = plt.subplots()
ax1.set_title('Tallas de especies')

ax1.boxplot(tallas,labels=especies)

plt.show()