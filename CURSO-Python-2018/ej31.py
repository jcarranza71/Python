# db
# SQLite: la base de datos queda integrada en el programa python
# no permite subconsultas ni FK
import sqlite3
conn=sqlite3.connect('db.db')
rs=conn.cursor()
rs.execute("DROP TABLE IF EXISTS usuarios;")
rs.execute('''
	CREATE TABLE usuarios(
		id integer primary key autoincrement,
		nombre varchar(128) unique,
		activo bool
		);
	''')
rs.execute("INSERT INTO usuarios (nombre) VALUES ('David'),('Ramón')")

usuarios=[
	('Juan',True),
	('Pepe',False),
	('Julián',True),
]
rs.executemany("INSERT INTO usuarios(nombre,activo) VALUES (?,?)",usuarios)

rs.execute("SELECT * FROM usuarios")
r=rs.fetchall()
for i in r:
	print(i)

conn.commit()
conn.close()