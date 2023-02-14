import sqlite3
import tkinter 
from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.title ("BD")
ventana.geometry ("450x300+590+320")
ventana.configure(bg= "black")
ventana.resizable(0,0)
Label(ventana, text = "ID:", bg = "yellow").pack()
caja1 = Entry(ventana)
caja1.pack()
Label(ventana, text = "NOMBRE:", bg = "yellow").pack()
caja2 = Entry(ventana, show = "")
caja2.pack()
Label(ventana, text = "APELLIDO:", bg = "yellow").pack()
caja3 = Entry(ventana, show = "")
caja3.pack()
Label(ventana, text = "DNI:", bg = "yellow").pack()
caja4 = Entry(ventana)
caja4.pack()
Label(ventana, text = "NUMERO.TELEFONO:", bg = "yellow").pack()
caja5 = Entry(ventana)
caja5.pack()
Label(ventana, text = "GMAIL:", bg = "yellow").pack()
caja6 = Entry(ventana)
caja6.pack()


cur = conn.cursor()
conn = sqlite3.connect('/home/alumno/BD_LAB_PROG_UGARTE/Alumno.db')

cur.execute('SELECT * FROM Alumno')
 
for row in cur:
#Realizo las operaciones oportunas
    def data_entry():
        c.execute("INSERT INTO Alumno VALUES(Gonzalo, Amador, 915810128, 4")
        conn.commit()
        c.close()
        conn.close()
    
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

cur.close()
ventana.mainloop()