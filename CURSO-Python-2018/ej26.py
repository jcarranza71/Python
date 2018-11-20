# serialización de un objeto ¡se necesita la definición de la clase para leer!

import pickle

class persona():
	nombre=''
	edad=0
	def datos(self):
		return self.nombre+'/'+self.edad

a=persona()
a.nombre='David'
a.edad='42'
print(a.datos())

fid=open('datos.bin','wb')
pickle.dump(a,fid)
fid.close()

fid=open('datos.bin','rb')
b=pickle.load(fid)
fid.close()

print(b.datos())