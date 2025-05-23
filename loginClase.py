from tkinter import *
from tkinter import messagebox
import sqlite3
import hashlib
import os
import sys

# PyInstaller usa esta función para localizar los recursos
def recurso_path(rel_path):
    try:
        base_path = sys._MEIPASS  # Carpeta temporal del .exe
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, rel_path)

def encriptar_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def logearse():
    mi_conexion = sqlite3.connect(recurso_path("BBDD11"))
    #mi_conexion = sqlite3.connect("BBDD11")
    mi_cursor=mi_conexion.cursor()
    mi_cursor.execute("""SELECT * FROM alumnos
                      WHERE usuario=? AND passwd=?""",
                      (contenido_usuario.get(),encriptar_password(contenido_passwd.get())))
    resultado=mi_cursor.fetchall()
    #print(resultado)
    if resultado:
        messagebox.showinfo("Usario","Login correcto")
        root.destroy()   
        #os.system("python sumaClase.py")  
        #os.startfile("Practica.pdf")
        #os.startfile("C:\\Users\\pemil\\Desktop\\BrowserSqlite.msi")
        #os.startfile("sumaClase.exe")
        os.startfile(recurso_path("sumaClase.exe"))

    mi_conexion.close()

root=Tk()

contenido_usuario=StringVar()
contenido_passwd=StringVar()

label_usuario=Label(root, text="Usuario")
label_usuario.grid(row=0, column=0, pady=10,padx=10)

entry_usuario=Entry(root,textvariable=contenido_usuario)
entry_usuario.grid(row=0, column=1, pady=10,padx=10)

label_password=Label(root, text="Password")
label_password.grid(row=1, column=0, pady=10,padx=10)

entry_password=Entry(root,textvariable=contenido_passwd, show=("*"))
entry_password.grid(row=1, column=1, pady=10,padx=10)

boton_login=Button(root,text="Login", command=logearse)
boton_login.grid(row=2, column=0, columnspan=2, pady=10,padx=10)


root=mainloop()