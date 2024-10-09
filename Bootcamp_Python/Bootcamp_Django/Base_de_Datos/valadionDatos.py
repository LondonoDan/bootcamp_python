import sqlite3 


def main():
    username = input("ingrese su nombre de usuario: ") # ambos son métodos para que el usuario ingrese datos
    password = input("Ingrese la contraseña: ")# getpass permite que el usuario ingrese datos, pero se debe importar
    
    if verificacionCredencial(username, password):
        print("Ingresaste los datos correctos... accediendo")
    
    else:
        print("No ingresaste los datos correctos, valida la información")
    
    
def verificacionCredencial(username, password): #se hace tdo el proceso en la funcion ya que ella va a permitir que valide los datos 
    conn = sqlite3.connect('miaplicacion.db') #asignando a una base de datos ya previamente creada
    cursor = conn.cursor()
    query = f"SELECT id FROM users WHERE username='{username}' AND password= '{password}'" #aqui estamos haciendo la validación y conectando con la base
    #lo que esta en minuscula son los nombres de mi tabla de datos
    #print("Query a ejecutar ",query) si queremos ver lo que estamos haciendo en la query
    rows = cursor.execute(query)    
    data = rows.fetchone()#rows.fetchone es un método el cual solo va a devolver un elemento, es decir 

    cursor.close() # no es necesario cerrarlo pero es una buena practica
    conn.close() # cerrando la conexion
    
    
    
    
    
    if data == None:  #esto nos permite que se retorne lo que indicamos en el if de arriba en verificaci...
        return False
    return True


if __name__== '__main__': #permite que la funcion main de arriba funcione con todo lo que le estamos indicando
    main()





