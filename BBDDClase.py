from tkinter import *
from tkinter import messagebox
import sqlite3
import hashlib

def encriptar_password(password)   :
    return hashlib.sha256(password.encode()).hexdigest()

#funciones
def crear():
    try:
        miconexion=sqlite3.connect("BBDD11")
        micursor=miconexion.cursor()
        micursor.execute("""CREATE TABLE alumnos
                     (id integer primary key autoincrement,
                     usuario varchar(20),
                     passwd varchar(20))""")
        miconexion.commit()
        miconexion.close()
        messagebox.showinfo("BBDD","Base de datos creada con éxito")
    except:
        messagebox.showinfo("BBDD","Base de datos ya existe")
def insertar():
    miconexion=sqlite3.connect("BBDD11")
    micursor=miconexion.cursor()
    micursor.execute("""INSERT INTO alumnos     
                     (usuario, passwd)VALUES(?,?)""",
                    (contenido_usuario.get(), encriptar_password(contenido_passwd.get())))
    miconexion.commit()
    miconexion.close()
    messagebox.showinfo("BBDD","Registro creadocon exito")                    
    
#Parte gráfica
root=Tk()
root.geometry("200x200")

contenido_usuario=StringVar()
contenido_passwd=StringVar()

label_id=Label(root,text="Id: ").pack()
entry_id=Entry(root).pack()

label_usuario=Label(root,text="Usuario: ").pack()
entry_usuario=Entry(root, textvariable=contenido_usuario).pack()

label_passwd=Label(root,text="Password: ").pack()
entry_passwd=Entry(root, textvariable=contenido_passwd, show=("*")).pack()

boton_crear=Button(root,text="Crear BBDD",command=crear).pack()

boton_insertar=Button(root,text="Insertar BBDD", command=insertar).pack()


root.mainloop()