import sqlite3
con = sqlite3.connect('datos.db')

cur = con.cursor()

# Create table
#cur.execute('''CREATE TABLE alumno(nombre text not null, apellido text not null, dni integer primary key not null, telefono numeric not null, gmail varchar(10) not null)''')

# Insert a row of data
cur.execute("INSERT INTO alumno VALUES ('46', 'Benjamin','Ajhuacho','46364521', '11457812', 'elpatron@gmail.com')")

# Guardar (confirmar) los cambios
con.commit()

# asegúrarse de que se hayan confirmado los cambios o se perderán.


# Nunca hagas esto - inseguro!
símbolo = 'ESO'
cur.execute("SELECT * FROM alumno WHERE simbolo = '%s'" % simbolo)

# Do this instead
t = ('ESO')
cur.execute('SELECT * FROM alumno WHERE simbolo=?', t)
print(cur.fetchone())

# insertar muchos registros a la vez
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
cur.executemany('INSERT INTO alumno VALUES (?,?,?,?,?)', purchases)

for row in cur.execute('SELECT * FROM alumno ORDER BY price'):
        print(row)



con.close()