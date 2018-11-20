# gui
# Radiobutton en vídeo 50
# Checkbutton en vídeo 51
from tkinter import *
from tkinter import messagebox
app=Tk()

# menú
def cerrar():
	salir=messagebox.askquestion('Salir','¿Deseas cerrar la aplicación?')
	if salir=='yes':
		app.destroy()
def acercade():
	messagebox.showinfo('Python test','v1.0')
ops=Menu(app)
app.config(menu=ops)
archivo=Menu(ops,tearoff=0)
archivo.add_command(label='Nuevo')
archivo.add_separator()
archivo.add_command(label='Cerrar',command=cerrar)
ayuda=Menu(ops,tearoff=0)
ayuda.add_command(label='Acerca de',command=acercade)
ops.add_cascade(label='Archivo',menu=archivo)
ops.add_cascade(label='Ayuda',menu=ayuda)

# formulario
frm=Frame(app,width=300,height=400)
frm.pack()

nombre=StringVar()
recordar=IntVar()
def procesa():
	nombre.set('David')
def recuerda():
	print(recordar.get())

foto=PhotoImage(file='figs/glasses.png')
Label(frm,image=foto).grid(row=5,column=0)
Label(frm,text='Nombre : ').grid(row=2,column=0,sticky='w',padx=10)
Label(frm,text='Contraseña : ').grid(row=3,column=0,sticky='w',padx=10)
Label(frm,text='Recordar usuario').grid(row=4,column=1,sticky='w',padx=10)
Label(frm,text='').grid(row=0,column=0)
Label(frm,text='').grid(row=8,column=0)
Entry(frm,fg='red',textvariable=nombre).grid(row=2,column=1,padx=10)
Entry(frm,fg='red',show='*').grid(row=3,column=1,pady=10)
Checkbutton(frm,text='',variable=recordar,onvalue=1,offvalue=0,command=recuerda).grid(row=4,column=0)
Button(frm,text='Enviar',width=15,command=lambda:procesa()).grid(row=5,column=1)

app.mainloop()