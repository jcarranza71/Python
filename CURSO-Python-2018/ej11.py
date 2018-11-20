# csv

import csv

def campo(t,c):
	r=[]
	campos=t[0]
	c=campos.index(c)
	for i in t:
		r.append(i[c])
	return r

a=[]
with open('ieo.txt', 'r') as csvfile:
    r = csv.reader(csvfile, delimiter=';')
    for i in r:
    	a.append(i)

b=[a[0]]
for i in a:
	if i[0]=='JULIO CESAR SAR VAZQUEZ':
		b.append(i)

print(len(b),'datos')
#print(b[0])

tallas=campo(b,'TALLA')
especies=campo(b,'ESP_CAT')

#print(especies)
#print(tallas)

c=[];
for i in range(len(especies)):
	c.append({
		'especie':especies[i],
		'talla':tallas[i],
		})
print(c)