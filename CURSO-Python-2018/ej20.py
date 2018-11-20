# insertar datos sinusoidales en excel

import numpy as np
import openpyxl
doc = openpyxl.load_workbook(
	'../data/test.xlsx')
x = np.linspace(0, 2 * np.pi, 20)
y = np.sin(x)
# recorro la variable y con un contador
for i in range(len(y)):
	coordenada='A'+str(i+1)
	print(coordenada,y[i])
	doc['Hoja2'][coordenada]=y[i]
doc.save('../data/test2.xlsx')