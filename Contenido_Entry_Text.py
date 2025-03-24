from tkinter import *
from tkinter import messagebox


def mostrar():
    nombre=contenido_nombre.get()
    messagebox.showinfo("Cuadro",nombre)
    label_resultado.config(text=nombre)
def mostrar2():
    #1 --> linea1, 0 --> caracter 0
    nombre2=cuadro_comentarios.get("1.0",END)
    messagebox.showinfo("Text",nombre2)
    label_resultado.config(text=nombre2)

root=Tk()

#variable
contenido_nombre=StringVar()

mi_frame=Frame(root)
mi_frame.pack()

label_nombre=Label(mi_frame,text="Nombre:")
label_nombre.grid(row=0,column=0,sticky="e",padx=10,pady=10)

cuadro_nombre=Entry(mi_frame, textvariable=contenido_nombre)
cuadro_nombre.grid(row=0,column=1,sticky="w",padx=10,pady=10)

cuadro_comentarios=Text(mi_frame, width=25, height=5)
cuadro_comentarios.grid(row=1,column=0,columnspan=2,padx=10,pady=10)

boton1=Button(mi_frame, text="Contenido del Entry",command=mostrar)
boton1.grid(row=2, column=0, padx=10,pady=10)

label_resultado=Label(mi_frame)
label_resultado.grid(row=3, column=0,columnspan=2, padx=10,pady=10)

boton2=Button(mi_frame, text="Contenido del Text",command=mostrar2)
boton2.grid(row=4, column=0,columnspan=2, padx=10,pady=10)


root.mainloop()