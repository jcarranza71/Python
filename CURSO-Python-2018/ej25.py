# serialización
# guardar en un fichero externo una colección, diccionario y hasta objeto
# pero codificado en código binario
# con el propósito de recuperarlo después
# pesa menos

import pickle

MiLista=['Pinta','Niña','Santa María']
print(MiLista)

fid=open('datos.bin','wb') # escritura binaria se pone b
pickle.dump(MiLista,fid)
fid.close()

del(MiLista)

fid=open('datos.bin','rb') # escritura binaria se pone b
MiLista=pickle.load(fid)
fid.close()

print(MiLista)