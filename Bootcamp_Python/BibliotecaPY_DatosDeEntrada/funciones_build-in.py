

# funcion filter, nos permite filtrar lo que deseemos
#aca vamos a filtrar los numeros pares
numeros= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def pares(x):
    if x % 2==0:
        return True
    
    return False

resultado= filter(pares, numeros)
print(list(resultado))

#vamos a filtrar por los paises que empiecen por la ho
paises = ["holanda", "brasil", "holanda", "colombia", "panama"]

def noRepetidos(x):
    if x == "ho":
        return False

    return True

resultado= filter(noRepetidos,paises)
print(list(resultado))

#aca vamos a usar la funcion set que nos permite eliminar los datos repetidos de una lista 
nuevalista=[]

pregunta = int(input("Cuantos paises desea agregar: "))


def Paises():
    for i in range(pregunta):
        pais= str(input(f"Ingrese el {i} pais: "))
        nuevalista.append(pais)
    nuevalista.sort()      
        
Paises()       

resultado= list(set(nuevalista))
resultado.sort()
print(resultado)

#funcion reduce y filter que nos ayuda a sumar los datos de una lista dada
from functools import reduce
numeros= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado= list(filter(lambda x: x % 2 ,numeros))
resultado.sort()
print(list(resultado))

print(f"suma de datos impares: {reduce(lambda a,b:a+b, resultado)}")








