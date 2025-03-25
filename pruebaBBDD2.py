from tkinter import *
from tkinter import messagebox
import sqlite3

def crear():
    try:
        miconexion=sqlite3.connect("BBDD10")
        micursor=miconexion.cursor()
        micursor.execute("""CREATE TABLE alumnos
                     (id integer primary key autoincrement,
                     usuario varchar(20),
                     passwd varchar(20))""")
        miconexion.commit()
        miconexion.close()
        messagebox.showinfo("BBDD","Base de datos creada con éxito")     
    except:
        messagebox.showinfo("BBDD","Base de Datos ya existe")
        
def insertar():
    miconexion=sqlite3.connect("BBDD10")
    micursor=miconexion.cursor()
    micursor.execute("""INSERT INTO alumnos
                     (usuario, passwd)VALUES(?,?)""",
                     (contenido_nombre.get(),
                      contenido_passwd.get()))   
    miconexion.commit()
    miconexion.close()
    messagebox.showinfo("BBDD","Registro insertado con éxito")

def actualizar():
    miconexion=sqlite3.connect("BBDD10")
    micursor=miconexion.cursor()
    micursor.execute("""UPDATE alumnos SET
                     usuario=?,
                     passwd=?
                     where id=?""",
                     (contenido_nombre.get(),
                      contenido_passwd.get(),
                      contenido_id.get()))    
    miconexion.commit()
    miconexion.close()
    messagebox.showinfo("BBDD","El registro se actualizo correctamente")

def leer():
    miconexion=sqlite3.connect("BBDD10")
    micursor=miconexion.cursor()
    micursor.execute("""SELECT * FROM alumnos
                     where id=?""",
                     (contenido_id.get()))
    resultado=micursor.fetchall()
    for i in resultado:
        contenido_id.set(i[0])
        contenido_nombre.set(i[1])
        contenido_passwd.set(i[2])
    #miconexion.commit()
    miconexion.close()
    

    
root=Tk()

#variables
contenido_id=StringVar()
contenido_nombre=StringVar()
contenido_passwd=StringVar()

mi_frame=Frame(root)
mi_frame.pack()

label_id=Label(mi_frame,text="id: ")
label_id.grid(row=0,column=0,padx=10,pady=10)

entry_id=Entry(mi_frame, textvariable=contenido_id)
entry_id.grid(row=0,column=1,padx=10,pady=10)

label_nombre=Label(mi_frame,text="Nombre: ")
label_nombre.grid(row=1,column=0,padx=10,pady=10)

entry_nombre=Entry(mi_frame, textvariable=contenido_nombre)
entry_nombre.grid(row=1,column=1,padx=10,pady=10)

label_passwd=Label(mi_frame,text="Password: ")
label_passwd.grid(row=2,column=0,padx=10,pady=10)

entry_passwd=Entry(mi_frame, textvariable=contenido_passwd, show=("*"))
entry_passwd.grid(row=2,column=1,padx=10,pady=10)

boton_crear=Button(mi_frame,text="Crear BBDD", command=crear)
boton_crear.grid(row=3,column=0,padx=10,pady=10)

boton_insertar=Button(mi_frame,text="Insertar BBDD", command=insertar)
boton_insertar.grid(row=3,column=1,padx=10,pady=10)

boton_actualizar=Button(mi_frame,text="Actualizar BBDD", command=actualizar)
boton_actualizar.grid(row=4,column=0,padx=10,pady=10)

boton_leer=Button(mi_frame,text="Leer BBDD", command=leer)
boton_leer.grid(row=4,column=1,padx=10,pady=10)



root.mainloop()