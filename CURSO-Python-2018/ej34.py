# funcion filter (funciones de orden superior, programación funcional)
# python es multiparadigma: POO y multifunción
# comprueba si los elementos de una lista cumplen una condición
# devolviendo un iterador con los elementos que la cumplen

# ej: devuelve número pares 

'''
def impar(num):
	if num%2:
		return True
'''

lista=[1,2,3,4,5,6,7,8,9]

impar = lambda num: num%2
print('impares: ',list(filter(impar,lista)))

print('pares: ',list(filter(lambda n:not(n%2),lista)))