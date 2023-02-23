import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3

ventana = tkinter.Tk()
ventana.geometry("450x250+500+250")
ventana.configure(bg="grey")
tabla_botones = []
bd = sqlite3.connect('fichaje.db')
cur = bd.cursor()

def guardar(): 
    nombre = caja3.get()
    apellido = caja4.get()
    club = caja6.get()
    dni = caja8.get()  
    sql = 'INSERT OR IGNORE INTO jugadores (nombre, apellido, club, dni) VALUES ("{}", "{}", "{}", "{}");'
    cur.execute(sql.format(nombre,apellido,club,dni))
    bd.commit()
    
    caja3.delete(0,"end")
    caja4.delete(0,"end")
    caja6.delete(0,"end")
    caja8.delete(0,"end")
    

def buscar(event):
    print("elegido",event)
    #sql = 'SELECT' USAR variable event
    #cur.execute(sql)
    resp = "OBTENER DATOS???? nombre-apellido-club-dni" 
    #resp hay que ponerla en las cajas
    

def llenar_combo():
    sql = 'SELECT dni,nombre,apellido,club from Jugadores;'
    cur.execute(sql)
    resp = cur.fetchall() #"OBTENER DATOS???? dni,nombre,apellido,club"
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

Label(ventana, text = "nombre:").pack()
caja3 = Entry(ventana)
caja3.pack()

Label(ventana, text = "apellido:").pack()
caja4 = Entry(ventana, show = "*")
caja4.pack()

Label(ventana, text = "club").pack()
caja6 = Entry(ventana)
caja6.pack()

Label(ventana, text = "dni:").pack()
caja8 = Entry(ventana, show = "*")
caja8.pack()

boton = ttk.Button(text="fichado", command = guardar)
boton.place(x=135, y=200)

#sql = 'SELECT dni from Jugadores;'
#cur.execute(sql)
resp = "OBTENER DATOS???? dni"
#resp hay que ponerla en OptionList


ventana.mainloop()