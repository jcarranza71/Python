# interfaz gráfica
# raíz, frame, widgets (el propio frame es un widget)

from tkinter import *

app=Tk()

app.title('Pruebas')
app.resizable(1,0) # redimensionar
app.iconbitmap('') # icono de la aplicación
app.geometry('800x600')
app.config(
	bg='blue',
	)
#app.print('hola mundo')
app.mainloop()