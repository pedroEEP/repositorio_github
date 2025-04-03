from tkinter import *
from tkinter import messagebox

def version():
    messagebox.showinfo("Menu","Version xxx")

root=Tk()
mi_menu=Menu(root)
root.config(menu=mi_menu, width=200, height=200)

archivo_menu=Menu(mi_menu, tearoff=0)
archivo_menu.add_command(label="Guardar")
archivo_menu.add_command(label="Guardar Como")

archivo_ayuda=Menu(mi_menu, tearoff=0)
archivo_ayuda.add_command(label="Version", command=version)

mi_menu.add_cascade(label="Archivo",menu=archivo_menu)
mi_menu.add_cascade(label="Ayuda",menu=archivo_ayuda)


root.mainloop()