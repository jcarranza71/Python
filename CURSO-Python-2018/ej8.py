# poo

class Coche():
	ruedas=4
	__velocidad=0
	def acelera(self):
		self.__velocidad+=1
	def frena(self):
		self.__velocidad-=1
	def velocimetro(self):
		return self.__velocidad

v1=Coche()
v2=Coche()
v1.ruedas=5
print(v1.velocimetro())
for i in range(5,10,1):
	print(i,end=' ')
	v1.acelera()
print('Debería ser 5: ',v1.velocimetro())
v1.frena()
print('Debería ser 4: ',v1.velocimetro())
print(v1.ruedas)
print(v2.ruedas)