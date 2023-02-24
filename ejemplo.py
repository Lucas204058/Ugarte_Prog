import sqlite3
from tkinter import ttk

con = sqlite3.connect('datos.db')

cur = con.cursor()

# Create table
#cur.execute('''CREATE TABLE alumno(nombre text not null, apellido text not null, dni integer primary key not null, telefono numeric not null, gmail varchar(10) not null)''')

# Insertar datos
#cur.execute("INSERT INTO alumno VALUES ('9', 'Roque', 'Portillo','45', '11457812', 'roqueportillo@gmail.com')")

# Guardar (confirmar) los cambios
con.commit()

# asegúrarse de que se hayan confirmado los cambios o se perderán.

# Nunca hagas esto - inseguro!
#cur.execute("SELECT * FROM alumno WHERE simbolo = '%s'" % simbolo)

# Do this instead
t = ('ESO')
#cur.execute('SELECT * FROM alumno WHERE simbolo=?', t)
print(cur.fetchone())

# insertar muchos registros a la vez
alumno = [('7', 'Axel','Garcia','46364521', '11457812', 'emo@gmail.com'),
             ('7', 'Lucas','Ugarte','46364521', '11457812', 'lucasugarte@gmail.com'),
             ('7', 'Benjamin','Ajhuacho', 46364521, 11457812, 'elpatro@gmail.com'),
            ]
#cur.executemany('INSERT INTO alumno VALUES (?,?,?,?,?,?)', alumno)

for row in cur.execute('SELECT * FROM alumno ORDER BY nombre'):
        print(row)


con.close()