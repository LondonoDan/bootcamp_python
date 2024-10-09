# Input / Output entrada y salida. 

numero=30
texto = "Dani"
estatura= 1.50

#varias formas de mostrar texto 1ra

print("Ella se lla {} tiene {} años y mide {} ".format(texto,numero,estatura))
print("💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥")

#2da forma, se le puede insertar a un texto funciones o ejemplo para poner la letra en mayuscula ejemplo
print("Vamos a imprimir todas las funciones que podemos usar")
import pprint
pprint.pprint(dir(""))
print("💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥")
cadena= "me encanta "
print(f" el helado {cadena.title()}") #Indica que ponga todas las primeras letras de la variable en mayusculas
saludo = "hola"
print(f"este es el saludo {saludo.upper()}") #esto indica que todo lo que esta en la variable cambia a mayuscula

print("💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥")
print(f"Ella se llama {texto} tiene {numero} y mide {estatura}")

#Tambien se puede con funciones ejemplo

def suma(a,b):
    return a+b
print(f"La suma es {suma(numero,numero)}")

#Otra forma de imprimir es 

txt= f"La suma es {suma(numero,numero)}"
print(txt)


#ejemplo formas de mostrar mensajes en clases  
#se usa para mostrar mensajes varias formas una de ellas es __str__ que se utiliza para describir objetos
# Y repr para cosas mas formales o tecnicas del objeto

print("💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥")
class juguete:          #Clase
    nombre=""
    precio=0.0
    
    
    def __init__(self,nombre,precio):  #Constructor
        self.nombre=nombre
        self.precio=precio
        
    def __str__(self): #Sobrecargar datos para mostrarlos con la funcion str 
        return f"Mi nombre es {self.nombre} y mi precio es {self.precio}"    
    
    def __repr__(self): #Sobrecargar datos para mostrarlos con la funcion repr se usa mas que todo para desarrolo y depuración
        return f"aca solo digo mi nombre {self.nombre}"
    
        
j1=juguete("loli",5.0)    #Instancia de la clase, creación del objeto

print(str(j1))
  
print(repr(j1))














































        
        

















