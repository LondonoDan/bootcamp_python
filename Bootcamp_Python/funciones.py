#una funcion es la forma de escribir codigo reutilizable, ya que en el programa puedes llamar
#las funciones creadas

#Ejemplo de función

def suma(a,b):
    return a + b
resultado =suma(5,6)
print(resultado)



print("////////////////////////////////")

#Se pueden declarar funciones dentro de otras funciones
#ejemplo

def matematicas(a,b):
    def sumar(a,b):
        print("El resultado de la suma es: ") 
        print(a+b)
        
    def resta (a,b):
        print("El resultado de la resta es: ")
        print(a-b)
    sumar(a,b)
    resta(a,b)


matematicas(5,1)

#funcion sumando una tupla, *args indica que es una tupla o lista

print("/////////////////////////////")
def suma(*args):
    resul=0
    
    for arg in args:
        resul+=arg
        
    print(resul)
    
suma(1,2,6,6,7)    

