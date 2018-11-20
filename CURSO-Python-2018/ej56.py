# mongoDB
# en c:\xampp\mongodb\bin
# mongod -dbpath data/db1

from pymongo import MongoClient

conn = MongoClient()

db = conn.pruebas

"""
db.pruebas.insert_one({
	'nombre': 'Pedro',
	'tlf': [
		666555444,
		666555333,
		],
	})
"""

a=db.pruebas.find()

for i in a:
	for j in i:
		print(j,': ',i[j])

#count deprecated
print('Registros insertados: ',db.pruebas.estimated_document_count())

#a=db.pruebas.find({'nombre':'Julián'}).explain()
#proyecto sólo los campos que quiero mostrar
a=db.pruebas.find({'nombre':'Pedro'},{'nombre':1,'_id':0})

a=db.pruebas.find({'tlf':666555444},{'nombre':1,'tlf':1,'_id':0})
#a=db.pruebas.find({'nombre':'Pedro'})
for i in a:
	print(i['tlf'][0])

# búsqueda por índices
# db.pruebas.createIndex({nombre:1})

#db.pruebas.delete_many({'nombre':'Julián'})