#Manipulación de ficheros, se usa mediante el comando nombre de la variable open y el comando
# f= open('/etc/cualquierfichero', 'r') la 'r' indica lo que planeas hacer en el fichero, es decir que si yo indico que voy
# voy a abrir un fichero con el permiso 'r' indica que solo lo voy a leer, si le indico que
# lo voy a abrir 'rw+' o 'rw' indica que se abrira de lectura y escritura.
# Read o write 
# write: agregar datos nuevos borra los que esten existentes. 
#writelines: deja ingresar varios caracteres como si fuera una lista
# readlineas= se utiliza para mostrar el contenido del fichero



#Permisos

# r= lectura 
# a: añadir datos a un fichero existente en la parte de abajo
# w: escritura  
# x: create

# t: texto
# b: binary

# + plus

print("💥💥💥💥💥💥 Vamos a leer un fichero 💥💥💥💥💥💥💥💥")

#ejemplo
#Vamos a crear un fichero nuevo sin datos
#m = open('nuevo.txt', 'x')
#m.close()

#agregar datos al fichero creado anteriormente o a cualquiera que ya este creado
m=open('nuevo.txt', 'w')
m.writelines(["Juan" "\nJose" "\nMatias"])
m.close()

#Estamos modificando un fichero  
f= open('nombres.txt', 'w') #Creando el fichero y este es el nombre que va a tener mas el permiso
f.write("Datos\n") # 
f.write("Datos2") # estamos agregando datos
f.close()


#c=open('ficheroEliminar.txt', 'x')  se pone como comentario para que el sistema no lo tome como que esta repetido
#c.close()

#Para eliminar un fichero puedes hacerlo importando la funcion os y luego el metodo remove()
#Ejemplo
#import os
#os.remove('ficheroEliminar.txt')

#Mostrar el contenido del fichero
m= open("nuevo.txt", 'r')
print(m.readlines())
m.close()

#Guardar la información de mi programa en un fichero se debe importar pickle
#ejemplo
print ("Estamos imprimiendo los datos del objeto guardado")
#Creacion del objeto
import pickle
class juego:
    nombre= ""
    edad = 0
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def getNom(self):
        return self.nombre

jugagor1 = juego("Daniela", 29)

#ahora lo vamos a guardar en un fichero para que la info qie ingreso el jugador 1 no se pierda
#i = open ("save.bin", 'wb')
#pickle.dump(jugagor1,i)
#i.close()

#Ahora vamos a acceder a el
i = open("save.bin", "rb")
datosGuardatos= pickle.load(i)
i.close()

print("El nombre del jugador1 es ",datosGuardatos.getNom(), "y la edad es de " ,datosGuardatos.edad)


if datosGuardatos.edad < 18:
    print("No puedes jugar eres menor de edad")
    
else:
    print("Puedes jugar eres mayor de edad")












    
    
    
    
    
    
    
    
    
    
    
    




















