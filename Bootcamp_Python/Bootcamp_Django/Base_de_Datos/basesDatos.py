import sqlite3 # se debe importar el aplicativo que permite trabajar con la base de datos


conn = sqlite3.connect('miaplicacion.db') #asignando a una base de datos ya previamente creada
cursor = conn.cursor() #creando el cursos para hacer consultas
rows= cursor.execute('SELECT * FROM users') #para hacer consultas en nuestra base de datos, aca vamos a validar los datos de mi tabla de users
#si queremos validar solo de una casilla en especifico, una forma es despues del SELECT + FROM users WHERE username="Daniela") 
for row in rows: #nos permite ver todos los datos de la tabla anclada, debemos siempre crear un bucle para ello
    print(row)







cursor.close() # no es necesario cerrarlo pero es una buena practica
conn.close() # cerrando la conexion