import sqlite3
#Vamos a validar los datos de una tabla

conn = sqlite3.connect('alumnos.db')
cursor = conn.cursor()
rows= cursor.execute('SELECT * FROM alumnos WHERE nombre="Daniela"')

for row in rows: #nos permite ver todos los datos de la tabla anclada, debemos siempre crear un bucle para ello
    print(row) 
    
    
cursor.close()
conn.close()    