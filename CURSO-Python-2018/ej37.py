# expresiones regulares

import re

pajar='vamos a aprender expresiones regulares en Python. Python es un lenguaje sencillo'
aguja='Python'

if re.search(aguja,pajar) is not None:
	print('Texto encontrado')
else:
	print('Texto no encontrado')


r=re.search(aguja,pajar)

print(r.start())
print(r.end())
print(r.span()[1])

print(len(re.findall(aguja,pajar)))