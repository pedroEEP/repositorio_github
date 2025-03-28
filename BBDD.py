from tkinter import *
from tkinter import messagebox
import sqlite3
import hashlib

def encriptar_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def crear():
    miconexion=sqlite3.connect("BBDD3")
    micursor=miconexion.cursor()
    try:
        micursor.execute("""CREATE TABLE alumnos
                     (id integer primary key autoincrement,
                     usuario varchar(20),
                     password varchar(20))
                     """)
        miconexion.commit()
        miconexion.close()
        messagebox.showinfo("BBDD","BBDD creada con éxito")
    except:
        messagebox.showinfo("BBDD", "La BBDD ya existe")

def insertar():
    miconexion=sqlite3.connect("BBDD3")
    micursor=miconexion.cursor()
    micursor.execute("""INSERT INTO alumnos (usuario, password) VALUES (?, ?)""",
                 (mi_usuario.get(), encriptar_password(mi_passwd.get())))
    miconexion.commit()
    miconexion.close()
    messagebox.showinfo("BBDD","Registro insertado con éxito")

    
root=Tk()
root.title("Prueba BBDD")

#Variables
mi_usuario=StringVar()
mi_passwd=StringVar()
mi_id=StringVar()

mi_frame=Frame(root)
mi_frame.pack()

label_usuario=Label(mi_frame,text="Usuario: ")
label_usuario.grid(row=1,column=0, padx=10,pady=10)

entry_usuario=Entry(mi_frame, textvariable=mi_usuario)
entry_usuario.grid(row=1,column=1, padx=10,pady=10)

label_passwd=Label(mi_frame,text="Password: ")
label_passwd.grid(row=2,column=0, padx=10,pady=10)

entry_passwd=Entry(mi_frame, textvariable=mi_passwd, show="*")
entry_passwd.grid(row=2,column=1, padx=10,pady=10)

label_id=Label(mi_frame,text="Id: ")
label_id.grid(row=0,column=0, padx=10,pady=10)

entry_id=Entry(mi_frame, textvariable=mi_id)
entry_id.grid(row=0,column=1, padx=10,pady=10)

boton1=Button(mi_frame,text="Crear BBDD", command=crear)
boton1.grid(row=3,column=0, padx=10,pady=10)

boton2=Button(mi_frame,text="Insertar BBDD", command=insertar)
boton2.grid(row=3,column=1, padx=10,pady=10)


root.mainloop()