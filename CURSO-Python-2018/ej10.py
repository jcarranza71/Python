# desarrollo del acceso a csv

import csv

a=[]
with open('ieo.txt', 'r') as csvfile:
    r = csv.reader(csvfile, delimiter=';')
    for i in r:
    	a.append(i)

print(type(a))
print(a[1][0])
print(len(a))

b=[]
for i in a:
	if i[0] not in b:
		b.append(i[0])		
print(b)