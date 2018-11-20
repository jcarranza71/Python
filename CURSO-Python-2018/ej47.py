# mongoDB
# mongod -dbpath data/db1

from pymongo import MongoClient

conn = MongoClient()

db = conn.pruebas


db.pruebas.insert_one({
	'nombre': 'Julián',
	'tlf': { 
		'tlf1': 666555444,
		'tlf2': 666555333,
		},

	})


a=db.pruebas.find()

for i in a:
	for j in i:
		print(j,': ',i[j])

#count deprecated
print('Registros insertados: ',db.pruebas.estimated_document_count())

#a=db.pruebas.find({'nombre':'Julián'}).explain()
a=db.pruebas.find({'nombre':'David'},{'nombre':1,'_id':0})
for i in a:
	print(i)

# búsqueda por índices
# db.pruebas.createIndex({nombre:1})

#db.pruebas.delete_many({'nombre':'Julián'})