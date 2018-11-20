# clases

class coche():
	ruedas=4
	__velocidad=0
	def acelera(self):
		self.__velocidad+=1
	def frena(self):
		self.__velocidad-=1
	def velocidad(self):
		return self.__velocidad


v=coche()
v.ruedas=5
print('Mi coche v tiene',v.ruedas,'ruedas')

print('Velocidad:',v.velocidad())
v.acelera()
v.acelera()
print('Velocidad:',v.velocidad())
v.frena()
print('Velocidad:',v.velocidad())