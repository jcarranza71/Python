# leer de una url

import io

#fid=open('http://www.elpais.es','r')
fid=open('datos.txt','r')
txt=fid.read()
fid.close()

print(txt)