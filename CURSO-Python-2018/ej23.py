# persistencia de datos
# ficheros y bases de datos
# también comentarios con triple comilla doble

import io

fid=open('datos.txt','w')
fid.write('Hola mundo,\nya escribo ficheros')
fid.close()


fid=open('datos.txt','a')
fid.write('\nAñado una última línea')
fid.close()

fid=open('datos.txt','r')
txt=fid.read()
fid.seek(0)
txt+=fid.read()
print(txt)
fid.close()

fid=open('datos.txt','r')
txt2=fid.readlines()
# también tenemos readlines
fid.close()

for i in txt2: print(i)

