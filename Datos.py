#Importaciones:
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3


#Ventanas:
ventana = tkinter.Tk()
ventana.title ("Mis Datos")
ventana.geometry("500x350+590+320")
ventana.configure(bg="black")
ventana.resizable(0,0)
tabla_botones = []
bd = sqlite3.connect('datos.db')
cursor = bd.cursor()


def guardar():
    id = caja1.get()
    nombre = caja2.get()
    apellido = caja3.get()
    dni = caja4.get()
    telefono = caja5.get()
    gmail = caja6.get()
    cursor.execute('INSERT INTO alumno VALUES ("{}", "{}", "{}", "{}", "{}", "{}")')
    print(id, nombre, apellido, dni, telefono, gmail)
    bd.commit()

#Insertar los datos.
#cur.execute("INSERT INTO alumno VALUES ('9', 'Roque','Portillo', '45', '11457812', 'roqueportillo@gmail.com')")


#Para que lo que se va insertando lo borre automaticamente, como en el caso de cajas y buscar.
def cajas(delete):
    caja1.delete(0,"end")
    caja2.delete(0,"end")
    caja3.delete(0,"end")
    caja4.delete(0,"end")
    caja5.delete(0,"end")
    caja6.delete(0,"end")
    

def buscar(delete):
    caja1.delete(0,END)
    caja2.delete(0,END)
    caja3.delete(0,END)
    caja4.delete(0,END)
    caja5.delete(0,END)
    caja6.delete(0,END)
       
    dni = combo.get()
    print(dni)
    query = ("SELECT * FROM alumno WHERE DNI = 46364521".format(dni))
    print(query)
    cur.execute(query)
    resp = cur.fetchall()
    print(resp)
    caja1.insert(0, resp[0][0])
    caja2.insert(0, resp[0][1])
    caja3.insert(0, resp[0][2])
    caja4.insert(0, resp[0][3])
    caja5.insert(0, resp[0][4])
    caja6.insert(0, resp[0][5])
 
 
#Para que pueda hacer una combinacion entre caja de textos y listas.
def llenar_combo():
    #Selecionar lo que estè dentro de la base de datos
    sql = 'SELECT Id, Nombre, Apellido, DNI, Telefono, Gmail from alumno;'
    cursor.execute(sql)
    resp = cursor.fetchall() #"OBTENER DATOS???? Id, Nombre, Apellido, DNI, Telefono, Gmail"
    #resp hay que ponerla en OptionList
    for i in resp:
        OptionList.append(i)
    #print("resp: ", OptionList)

OptionList = []

llenar_combo()


#Caja de textos.
Label(ventana, text = "ID:", bg = "yellow").pack()
caja1 = Entry(ventana, show = "")
caja1.pack()

Label(ventana, text = "Nombre:", bg = "grey").pack()
caja2 = Entry(ventana, show = "")
caja2.pack()

Label(ventana, text = "Apellido:", bg = "green").pack()
caja3 = Entry(ventana, show = "")
caja3.pack()

Label(ventana, text = "DNI:", bg = "white").pack()
caja4 = Entry(ventana, show = "")
caja4.pack()

Label(ventana, text = "Telefono:", bg = "pink").pack()
caja5 = Entry(ventana, show = "")
caja5.pack()

Label(ventana, text = "Gmail:", bg = "orange").pack()
caja6 = Entry(ventana, show = "")
caja6.pack()


#sql = 'SELECT DNI from alumno;'
#cur.execute(sql)
respuesta = "OBTENER DATOS???? dni"
#respuesta hay que ponerla en OptionList


for row in cursor.execute('SELECT * FROM alumno ORDER BY Nombre'):
        print(row)


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


#Lista Desplegable.
lista = ["Axel", "Benjamin", "Roque", "Lucas", "Sofia"]
combo = ttk.Combobox(values = lista)
combo.place(x=165, y=250)


#Botones:
boton1 = tk.Button(text="Guardar", relief="ridge", borderwidth=5, command = guardar)
boton1.place(x=165, y=280)

boton2 = tk.Button(text="Buscar", relief="ridge", borderwidth=5,  command = textocaja)
boton2.place(x=270, y=280)


#Para cerrar la ventana.
ventana.mainloop()