# funciona lambda

#def potencia(base,exp):
#	return base**exp

potencia = lambda base,exp: base**exp
formatea = lambda txt: "¡{}!".format(txt)

print(potencia(2,4))
print(formatea('hola mundo'))