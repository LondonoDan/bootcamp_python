#Matriz creada de n*n 

fila = int (input("Introduce los días: "))          #Solicitando de cuantas filas sera
columna = int (input("Cuantas vacas tienes?: "))    #Solicitando de cuantas columnas sera

matriz=[] #En esta matriz se van a cargar los datos que el usuario ingrese

for i in range (fila): #Aca estamos cargando los datos que el usuario esta ingresando por teclado
    matriz.append([])
    for j in range (columna):
        valor= float(input("fila {}, columna {}: ".format(i+1, j+1))) #Aca estamos dando permiso para que el usuario agrege el dato que va en la matriz, adicional se le dice el número de fila y columna
        matriz[i].append(valor)  #Se carga el dato que el usuario agregue a la matriz
        
        
print()

for fila  in matriz: #Aca estamos imprimiendo la matriz
    print("[",end=" ")
    for elemento in  fila:
        print("{:8.2f}".format(elemento), end="")
        print("]")
print()                

