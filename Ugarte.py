import sqlite3
import tkinter 
from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.title ("Mis Datos")
ventana.geometry ("450x300+590+320")
ventana.configure(bg= "Black")

Label(ventana, text = "ID:", bg = "yellow").pack()
caja1 = Entry(ventana)
caja1.pack()
Label(ventana, text = "NOMBRE:", bg = "grey").pack()
caja2 = Entry(ventana, show = "")
caja2.pack()
Label(ventana, text = "APELLIDO:", bg = "green").pack()
caja3 = Entry(ventana, show = "")
caja3.pack()
Label(ventana, text = "DNI:", bg = "white").pack()
caja4 = Entry(ventana)
caja4.pack()
Label(ventana, text = "NUMERO.TELEFONO:", bg = "pink").pack()
caja5 = Entry(ventana)
caja5.pack()


conn = sqlite3.connect('/home/alumno/Ugarte_prog/Alumno.db')
cur = conn.cursor()


cur.execute('SELECT * FROM Alumno')
 
for row in cur:
#Realizo las operaciones oportunas
    def data_entry():
        c.execute("INSERT INTO Alumno VALUES(Lucas, Ugarte, 915810128, 4)")
        conn.commit()
        c.close()
        conn.close()
    
def textocaja():
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

cur.close()
ventana.mainloop()