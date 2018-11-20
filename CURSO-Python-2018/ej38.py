# anclas, rangos

import re

nombres=[
	'Ana Gómez',
	'María Martín',
	'Sandra López',
	'Santiago Mortín',	
]

print('---- Comienzan en San')
for i in nombres:
	if re.findall('^San',i):
		print(i)

print('---- Terminan en ín')
for i in nombres:
	if re.findall('ín$',i):
		print(i)

print('---- Contiene ra')
for i in nombres:
	if re.findall('M[a-o]rtín',i):
		print(i)

