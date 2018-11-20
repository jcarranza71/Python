# diccionario

a={
	'nombre': 'David',
	'edad': 42,
	'deporte': {
		'deporte1':'natación',
		'deporte2':'bici',
	}
}

print(a['deporte']['deporte1'])
print(a)
print(a.items())
print(a.get('nombre'))
print(a['nombre'])
a.update({'nombre':'Julián'})
print(a)
a['nombre']='Pedro';
print(a)
print(type(a))
b='5'
c=int(b)
print(type(c))
c=1
print(type(c))