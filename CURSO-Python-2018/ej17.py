# xml

import untangle


r = untangle.parse('https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml')

for i in r.gesmes_Envelope.Cube.Cube.Cube:
	if i['currency']=='USD':
		print(i['currency'],i['rate'])
		cambio=i['rate']

print('El dolar está a ',cambio,' EUR')
#print(r.gesmes_Envelope.Cube.Cube)

txt='El dolar está a '+cambio+' EUR'
f=open('c:/xampp/htdocs/divisas.html','w')
f.write(txt)

f.close()