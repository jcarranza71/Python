# mongoDB
# en c:\xampp\mongodb\bin
# mongod -dbpath data/db1
# mongod -dbpath data/db1 --storageEngine=mmapv1

from pymongo import MongoClient

conn = MongoClient('172.24.0.232',27017)
#conn = MongoClient()
db=conn.pruebas
"""
db.pruebas.insert_one({
	'nombre':'David',
	'tlf':[
		647290540,
		942528940,	
		],
	'email':'dblanco@alpeformacion.es',
	})
"""
a=db.pruebas.find(
	{'nombre':'Amaia'},{'tlf':1,'_id':0})
for i in a:
	print(i)