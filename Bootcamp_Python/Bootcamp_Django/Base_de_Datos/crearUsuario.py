import sqlite3 

#vamos a crear una funcion para agregar un usuario a una tabla de datos ya creada. 
def main():      
    crearUsuadio(5,"pepe","345")



def crearUsuadio(id,username,password):
    conn = sqlite3.connect('miaplicacion.db', isolation_level=None ) #aqui estamos anclando la base de datos a la que queremos acceder para agregar los datos, isolation_lavel=None permite agregar datos asi esten repetidos
    cursor = conn.cursor()    
    query = '''INSERT INTO users(id, username,password) VALUES(?, ?, ?)'''
    rows = cursor.execute(query, (id, username, password))
    conn.commit() #cuando se hacen operaciones con INSERT O DELETE, debemos usar este comando para que funcione    
    
    cursor.close() # no es necesario cerrarlo pero es una buena practica
    conn.close() 
    
    
    
if __name__== '__main__': #permite que la funcion main de arriba funcione con todo lo que le estamos indicando
    main()
    
    
    
#SI SE VALIDA EN LA TABLA CREADA (miaplicacion.db), podemos validar que los datos que indicamos agregar estan alli    