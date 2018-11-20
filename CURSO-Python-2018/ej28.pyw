# interfaz gráfica
# raíz, frame, widgets (el propio frame es un widget)
from tkinter import *
app=Tk()
app.title('Pruebas')
#app.resizable(1,0) # redimensionar
app.iconbitmap('') # icono de la aplicación
app.geometry('800x600')
app.config(
	bg='white',
	)
frm=Frame()
frm.pack(
	#anchor='n', 	# con puntos cardinales
	#side='left',
	#expand=1, 		# 
	#fill='both', 	# ocupa todo el tamaño de la ventana
	)
frm.config(
	bg='red',
	width='400',
	height='300',
	bd=5,			# grosor del borde
	#relief='groove',
	relief='sunken',
	#cursor='hand2',
	#cursor='pirate',
	)
lbl=Label(frm,
	text='Hola mundo',
	fg='red',
	font=18,
	)
lbl.place(x=100,y=50)
Label(frm,
	text='Adiós mundo',
	font=('Courier New', 20)
	).place(x=200,y=100)
app.mainloop()