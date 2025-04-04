from tkinter import *
from tkinter import messagebox

def sumar():
    num1=int(numero1.get())
    num2=int(numero2.get())
    messagebox.showinfo("Suma",f"La suma total es: {num1+num2} ")

root=Tk()

numero1=StringVar()
numero2=StringVar()

root.geometry("150x150")

label_num1=Label(root, text="Numero1")
label_num1.pack()

entry_num1=Entry(root, textvariable=numero1)
entry_num1.pack()

label_num2=Label(root, text="Numero2")
label_num2.pack()

entry_num2=Entry(root,textvariable=numero2)
entry_num2.pack()

boton_suma=Button(root,text="Sumar", command=sumar)
boton_suma.pack( pady=20)

root.mainloop()