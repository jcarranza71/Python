# función map (funciones de orden superior)

# aplica una función a cada elemento de una lista iterable (lista, tupla, ...)
# devolviendo una lista con los resultados

# filter aplica una condición (construida incluso con una función lambda)
# map, en vez de una condición, aplica una función


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
	empleado('Juan','Director',6700),
	empleado('Ana','Presidente',7500),
	empleado('Antonio','Administrativo',2100),	
	empleado('Sara','Secretaria',2150),	
	empleado('Mario','Botones',1800),	
]

def comision(empleado):
	empleado.salario*=1.03
	return empleado

resultados=map(comision,empleados)
# curioso: si no guardas el resultado de map en una variable, no modifica la lista original

for emple in resultados:
	print(emple)

for emple in empleados:
	print(emple)