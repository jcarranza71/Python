# csv

import csv

def campo(t,c):
	r=[]
	campos=t[0]
	c=campos.index(c)
	print(c)
	for i in t:
		if i[c] not in r:
			r.append(i[c])
	return r

a=[]
with open('ieo.txt', 'r') as csvfile:
    r = csv.reader(csvfile, delimiter=';')
    j=0
    for i in r:
    	a.append(i)

print(a[0])
print(type(a))
print(a[0][0])

for i in range(len(a[0])):
	print(campo(a,a[0][i]))

