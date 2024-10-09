#Vamos a eliminar los datos repetidos que ingrese el usuario

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
