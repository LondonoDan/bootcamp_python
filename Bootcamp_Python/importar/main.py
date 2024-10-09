
#Importaciones o modulos, es cuando traemos o importamos información de otra carpeta, solo se debe importar clases y funciones. 
import operaciones 


def main():
    sum = operaciones.suma(2, 2) #Importando una funcion
    print("El resultado de la suma es: ",sum)
    
    
    res= operaciones.resta(4,6)
    print("El resultado de la resta es de ",res)
    
    multi = operaciones.multiplicacion(5,5)
    print("El resultado de la multiplicación es: ",multi)
 
 
 
 
 
    
if __name__ == '__main__': #Se debe crear esto siempre con el nombre de la carpeta para que funcione. 
    main()    