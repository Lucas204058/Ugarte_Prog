import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3

ventana = tkinter.Tk()
ventana.title ("Mis Datos")
ventana.geometry("500x350+590+320")
ventana.configure(bg="black")
ventana.resizable(0,0)
tabla_botones = []
bd = sqlite3.connect('datos.db')
cur = bd.cursor()

def guardar():
    id = caja2.get()
    nombre = caja3.get()
    apellido = caja4.get()
    dni = caja6.get()
    telefono = caja8.get()
    gmail = caja9.get()
    sql = 'INSERT OR IGNORE INTO alumno (Id, Nombre, Apellido, DNI, Telefono, Gmail) VALUES ("{}", "{}", "{}", "{}");'
    cur.execute(sql.format(Id, Nombre, Apellido, DNI, Telefono, Gmail))
    bd.commit()

# Insertar los datos
cur.execute("INSERT INTO alumno VALUES ('46', 'Benjamin','Ajhuacho','46364521', '11457812', 'elpatron@gmail.com')")


    caja2.delete(0,"end")
    caja3.delete(0,"end")
    caja4.delete(0,"end")
    caja6.delete(0,"end")
    caja8.delete(0,"end")
    caja9.delete(0,"end")
    

def buscar(event):
    print("Elegido",event)
    #sql = 'SELECT' USAR variable event
    #cur.execute(sql)
    resp = "OBTENER DATOS???? Id, Nombre-Apellido-DNI-Telefono-Gmail" 
    #resp hay que ponerla en las cajas
    

def llenar_combo():
    sql = 'SELECT Id, Nombre, Apellido, DNI, Telefono, Gmail from alumno;'
    cur.execute(sql)
    resp = cur.fetchall() #"OBTENER DATOS???? Id, Nombre, Apellido, DNI, Telefono, Gmail"
    #resp hay que ponerla en OptionList
    for i in resp:
        OptionList.append(i)
    #print("resp: ", OptionList)

OptionList = []

llenar_combo()

variable = tk.StringVar(ventana)
variable.set("Elegir")

opt = tk.OptionMenu(ventana, variable, *OptionList, command = buscar)
opt.config(width=50, font=('Helvetica', 12))
opt.pack()

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


#sql = 'SELECT dni from alumno;'
#cur.execute(sql)
resp = "OBTENER DATOS???? dni"
#resp hay que ponerla en OptionList

()


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


ventana.mainloop()