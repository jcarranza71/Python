# xls 2 python
# pip install openpyxl

import openpyxl
doc = openpyxl.load_workbook(
	'../data/test.xlsx')

for i in doc:
	for j in i:
		for k in j:
			print(i,k.coordinate,k.value)

print(doc['test1']['A1'].value)
doc['test1']['A1'].value=15
print(doc['test1']['A1'].value)
# i hojas
# j filas
# k celdas

doc.save('../data/test2.xlsx')