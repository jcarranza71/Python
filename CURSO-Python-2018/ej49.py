# arrays

a=[1,2,'hola',3]

a.append('fin')
a.insert(0,'insercion')
a.extend(['penúltimo','último'])
print(a[3])
print(a.index('hola'))
print('hola' in a)
print(a)
print(a.pop())
print(a[5:])


print(a)
a+=[1,2,3]
a.remove('hola')
print(a)

for i in a:
	print(i,', ',end='')

