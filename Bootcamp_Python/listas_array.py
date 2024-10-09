
#listas, para saber la longitud de la lista se puede validar con .length
#ejemplo


lista=[1,2,4,5,6,6]
longitud= len(lista)


print("Se van a imprimir la cantidad y el nùmero de posiciòn de la lista")
for i in range(longitud):
    print("tiene ",i, "posiciones")
    
print("Se van a imrpimir los datos de la lista")
print(lista)    


#Array solicitando datos a usuario

arreglo=[]
maximo=3
for i in range(maximo):
        
        nombre= str (input("Ingrese el nombre: "))
        arreglo.append(nombre)
        
        
print(arreglo)        


    