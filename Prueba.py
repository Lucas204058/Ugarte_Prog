#Importar nuestra librería
import sqlite3
import tkinter 
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import ttk


#Crear nuestra primera base de datos
def escribir_informacion():
    Id = caja1.get()
    Nombre = caja2.get()
    Apellido = caja3.get()
    DNI = caja4.get()
    Telefono = caja5.get()
    Gmail = caja6.get()
    bd = sqlite3.connect('datos.bd')
    cursor = bd.cursor()
    cursor.execute('INSERT OR IGNORE INTO alumno(Id, Nombre, Apellido, DNI, Telefono, Gmail) VALUES ("{}", "{}", "{}", "{}");'.format(Id, Nombre, Apellido, DNI, Telefono, Gmail))
    print(Id, Nombre, Apellido, DNI, Telefono, Gmail)
    bd.commit()

#Ventana principal
ventana = Tk()
ventana.title ("Mis Datos")
ventana.geometry ("500x350+590+320")
ventana.configure(bg= "Black")
ventana.resizable(0,0)
tabla_botones = []

#Caja de textos
Label(ventana, text = "ID:", bg = "yellow").pack()
caja1 = Entry(ventana)
caja1.pack()

Label(ventana, text = "Nombre:", bg = "grey").pack()
caja2 = Entry(ventana, show = "")
caja2.pack()

Label(ventana, text = "Apellido:", bg = "green").pack()
caja3 = Entry(ventana, show = "")
caja3.pack()

Label(ventana, text = "DNI:", bg = "white").pack()
caja4 = Entry(ventana)
caja4.pack()

Label(ventana, text = "Telefono:", bg = "pink").pack()
caja5 = Entry(ventana)
caja5.pack()

Label(ventana, text = "Gmail:", bg = "orange").pack()
caja6 = Entry(ventana)
caja6.pack()


def textocaja():
    text20 = caja6.get()
    print(text20)
    text20 = caja5.get()
    print(text20)
    text20 = caja4.get()
    print(text20)
    text20 = caja3.get()
    print(text20)
    text20 = caja2.get()
    print(text20)
    text20 = caja1.get()
    print(text20)

#Botones
boton1 = tkinter.Button(ventana, text = "Guardar", relief="ridge", borderwidth=5, command = textocaja)
boton1.place(x=200, y=300)
boton1.pack()


boton2 = tkinter.Button(ventana, text = "Buscar", relief="ridge", borderwidth=5, command = textocaja)
boton2.place(x=200, y=300)
boton2.pack()

ventana.mainloop()