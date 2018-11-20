# gui: manejo de archivos
from tkinter import *
from tkinter import filedialog
app=Tk()
def abre():
	fid=filedialog.askopenfilename(
		title='Abrir',
		#initialdir='c:/',
		filetype=(
			('Texto plano','*.txt'),
			('Todos','*.*'),
			))
	print(fid)
Button(app,text='Abrir ...',command=abre).pack()
app.mainloop()