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
    bd.commit()
    cur.execute(query)
    resp = cur.fetchall()
    print(resp)
    
    caja1.insert(0, resp[0][0])
    caja2.insert(0, resp[0][1])
    caja3.insert(0, resp[0][2])
    caja4.insert(0, resp[0][3])
    

# Insertar los datos
#cur.execute("INSERT INTO alumno VALUES ('46', 'Benjamin','Ajhuacho','46364521', '11457812', 'elpatron@gmail.com')")

# insertar muchos registros a la vez
alumno = [('7', 'Axel','Garcia','46364521', '11457812', 'emo@gmail.com'),
             ('7', 'Lucas','Ugarte','46364521', '11457812', 'lucasugarte@gmail.com'),
             ('5', 'Benjamin','Ajhuacho', 46364521, 11457812, 'elpatron@gmail.com'),
             ('54', 'Yair','Sanchez','yairsanchez@gmail.com', '1145781245', '45123789'),]

#cur.executemany('INSERT INTO alumno VALUES (?,?,?,?,?,?)', alumno)

for row in cur.execute('SELECT * FROM alumno ORDER BY nombre'):
        print(row)

def borrar(delete):
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
variable.set("Elegir dato")

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
boton1 = tkinter.Button(ventana, text = "Guardar", relief="ridge", borderwidth=5, command = guardar)
boton1.place(x=200, y=300)
boton1.pack()


boton2 = tk.Button(ventana, text="Buscar", relief="ridge", borderwidth=5,  command = buscar)
boton2.place(x=250, y=220)
boton2.pack()


ventana.mainloop()