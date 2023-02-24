import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3

def guardar():
    nombre = caja1.get()
    apellido = caja2.get()
    dni = caja3.get()
    colorfavorito = caja4.get()    
    cur.execute('INSERT OR IGNORE INTO Datos(Nombre, Apellido, DNI, ColorFavorito) VALUES ("{}", "{}", {}, "{}");'.format(nombre, apellido, dni, colorfavorito))
    print(nombre, apellido, dni, colorfavorito)
    bd.commit()
   
def buscar():
    
    caja1.delete(0, END)
    caja2.delete(0,END)
    caja3.delete(0,END)
    caja4.delete(0,END)
    
    
    dni = combo.get()
    print(dni)
    query = ("SELECT * FROM Datos WHERE DNI = {}".format(dni))
    print(query)
    cur.execute(query)
    resp = cur.fetchall()
    print(resp)
    caja1.insert(0, resp[0][0])
    caja2.insert(0, resp[0][1])
    caja3.insert(0, resp[0][2])
    caja4.insert(0, resp[0][3])
    
#CREAR VENTANA
bd = sqlite3.connect('datos1.bd')
cur = bd.cursor()
cur.execute("SELECT DNI FROM datos")
resp = cur.fetchall()
print(resp)

ventana = tkinter.Tk()
ventana.title("DATOS")
ventana.geometry("400x300+500+280")
ventana.configure(bg= "SpringGreen2")
ventana.resizable(0,0)
tabla_botones = []

#CAJAS DE TEXTOS
Label(ventana, text = "Nombre:", bg= "SpringGreen2").pack()
caja1 = Entry(ventana)
caja1.pack()

Label(ventana, text = "Apellido:", bg= "SpringGreen2").pack()
caja2 = Entry(ventana)
caja2.pack()

Label(ventana, text = "DNI:", bg= "SpringGreen2").pack()
caja3 = Entry(ventana)
caja3.pack()

Label(ventana, text = "Color Favorito:", bg= "SpringGreen2").pack()
caja4 = Entry(ventana)
caja4.pack()

   
#DESPLEGABLE

combo = ttk.Combobox(values=resp)
combo.place(x=115, y=185)


#CREAR BOTON
boton = tk.Button(text="Guardar", relief="ridge", borderwidth=5, command = guardar)
boton.place(x=110, y=220)

boton = tk.Button(text="Buscar", relief="ridge", borderwidth=5,  command = buscar)
boton.place(x=210, y=220)


ventana.mainloop()