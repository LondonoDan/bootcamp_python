#Vamos a insertar datos en la tabla 

import sqlite3 
#Función para agregar datos a una tabla
def main():      
    crearUsuario(115,"Ramón","Londi")



def crearUsuario(id,nombre,apellido):
    conn = sqlite3.connect('alumnos.db', isolation_level=None ) #aqui estamos anclando la base de datos a la que queremos acceder para agregar los datos, isolation_lavel=None permite agregar datos asi esten repetidos
    cursor = conn.cursor()    
    query = '''INSERT INTO alumnos(id, nombre,apellido) VALUES(?, ?, ?)'''
    rows = cursor.execute(query, (id, nombre, apellido))
    conn.commit() #cuando se hacen operaciones con INSERT O DELETE, debemos usar este comando para que funcione    
    
    cursor.close() # no es necesario cerrarlo pero es una buena practica
    conn.close() 
       
    
    
if __name__== '__main__': #permite que la funcion main de arriba funcione con todo lo que le estamos indicando
    main()



