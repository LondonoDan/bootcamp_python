#un objeto es una instancia de una clase
#Clases dinamicas y estaticas, dinamica siempre cuenta con la palabra self, estatica no la necesita
#crearemos una clase
#si una variable empieza con un guion bajo, no debemos modificarla fuera de la clase
#los constructores se usan para asignar nuestros atructos

class Lampara:
    #crearemos una propiedad 
    encendido = True
    apagado= False
    nombre = ""
    
    # Constructor: el constructor sirve para inicializar las variables, cuando tenemos propiedades y/o parametros
    def __init__(self, nombre):
        self.nombre= nombre
      
    #retornando el contenido del nombre   
    def getNombre(self):
        return self.nombre 
       
      
        
    #método DINAMICA
    def enciende(self):
        self.encendido = print("Encendido.... de color 💜")
        
    def apaga(self):
        self.apagado = print("Apagando...")
            
    
    
#Creando el Objeto
lampara1= Lampara("lampara de lava")

#Imprimiendo el atributo
print("❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️")
print(lampara1.encendido)

print("❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️")
#Imprimiendo el método
print("Se esta imprimiendo el método")
lampara1.enciende()
lampara1.apaga()

#Mostrando el contenido
print(lampara1.getNombre())  

print("❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️")

#  Herencia: indica que un objeto hijo puede heredar de otra padre sus propiedades y métodos
# se crea una clase padre, luego se crea la clase hijo y entre parentesis se pone el nombre de la clase padre. Ejemplo

class Bluetoth(Lampara):
    
    
    #Métodos y/o acciones
    def ON(self):
        print("Reproduciendo musica...🎼🎼")
        
    def OFF(self):   
        print("Apagando musica... 🔕 ")
        
        
lampara1= Bluetoth()
lampara1.ON()
lampara1.enciende()



#Clases abstractas: no podemos instanciar una clase abstracta, tendremos que derivarla si queremos crear un objeto que obtenga esos metodos
#La clase abstracta sirve para definir un conjunto de funciones comunes a otras clases, es decir, que si yo
#marco una clase como abstracta las demas clases que hereden de la clase abstracra deben tener los mismos metodos
#pueden emplearse de diferentes maneras, pero debe contener la misma cantidad de metodos
#Ejemplo

print("ESTAMOS EN LA CLASE ABSTRACTA")
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass
    
    
    
class Perro(Animal):
    def sonido(self):
        print("GuaGua 🦮🐶🦮🐶🦮🐶")    
        
    def movimientoCola(self):
        print("Moviendo la cola! 🐩 🐩 🐩 ")    
        
class Gato(Animal):
    def sonido(self):
        print("Miau Miau 🐱 🐈 🐱 🐈 🐱 🐈 ")  
        
    def ronroneo(self):
        print("RRRRRRRRRR🐈🐈🐈🐈")          
        
    def movimiendoCola(self):
        print("Moviendo colita de lado a lado despacio")

        
    
perro =Perro() #Instancia de la clase abstacta
perro.sonido()
perro.movimientoCola() 
gato = Gato()
gato.sonido()  
gato.ronroneo() 
gato.movimiendoCola()
    
# Relaciones HAS - A: Significa contiene, es decir composición, indica que una clase esta compuesta de otras clases
#Ejemplo es como si fuera una base de datos que se relcionan entre si algunos datos o en este caso clases 




class categorias:
    idCategoria = 0
    nombreCategoria = "cualquiera"
    
    
    
   
class proveedores:
    idProveedor = 0
    nombreProveedor = "Emilio"    
    
    
class productos:
    idproducto = 0
    categoriaProducto = categorias() #Estoy indicando que esta propiedad tiene relacion con lo que esta en la clase categorias
    precio= 0
    tamaño=0
    tipoProducto= 0
    cifProveedor= proveedores() #Esta indicando que este atributo tiene relacion o hereda lo que esta dentro de la clase proveedores
    

p = productos()  #Creando objeto o instanciando clase productos
    
print("Nombre del proveedor: "+p.cifProveedor.nombreProveedor) #Estamos mostrando los datos de la clase producto 

    
 
 
 
 
    
    
            
    
    







     
    
    
        





















        


        
















