# filter con clases

class empleado:
	def __init__(self,nombre,cargo,salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario
	def __str__(self):
		return '{} que trabaja de {} factura {} €'.format(
			self.nombre,self.cargo,self.salario
			)

empleados=[
	empleado('Juan','Director',75e3),
	empleado('Ana','Presidente',85e3),
	empleado('Antonio','Administrativo',25e3),	
	empleado('Sara','Secretaria',27e3),	
	empleado('Mario','Botones',21e3),	
]

salarios_altos=filter(lambda this: this.salario>50e3,empleados)

for emple in salarios_altos:
	print(emple)