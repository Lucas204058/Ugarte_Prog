#Importar nuestra librería
import sqlite3
import tkinter 
from tkinter import *
from tkinter import messagebox as MessageBox


#Crear nuestra primera base de datos
conexion = sqlite3.connect("datos.db")

cursor = conexion.cursor()

#cursor.execute("CREATE TABLE IF NOT EXISTS alumno(id INTEGER PRIMARY KEY NOT NULL, nombre VARCHAR(100) NOT NULL, apellido VARCHAR(100) NOT NULL, gmail VARCHAR(10) NOT NULL, telefono NUMERIC NOT NULL, dni VARCHAR(10) NOT NULL)")

cursor.execute("SELECT * FROM alumno")

conexion.commit()

ventana = Tk()
ventana.title ("Mis Datos")
ventana.geometry ("450x300+590+320")
ventana.configure(bg= "Black")

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
Label(ventana, text = "Gmail:", bg = "pink").pack()
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
    
boton1 = tkinter.Button(ventana, text = "Guardar", command = textocaja)
boton1.pack()


conexion.close()
ventana.mainloop()