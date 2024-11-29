from tkinter import *

ventana = Tk()
ventana.title("Hola Mundo")
ventana.geometry=("800x400")

lbl=Label(ventana,text="Este es un Label")
lbl.pack()

btn  = Button(ventana,text="Presionar")
btn.pack()

ventana.mainloop()
