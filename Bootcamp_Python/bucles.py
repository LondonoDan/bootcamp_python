#Bucles

#siempre se va a ejecutar mientras la accion sea verdadera
#para concatenar variables es con , o con f{}
#Palabra reservada break y continue

#es igual al if, la diferencia es que se repite hasta el nùmero dado 
contador=1
while contador <=5:
    #print("El nùmero es: ",contador);
    print(f"El nùmero es: {contador}")
    
    contador+=1  
    
print("////////////////////////////////////////////////////")    
    
#ejecicion de los nùmeros pares con while
cont=1
while cont <=10:
    if cont %2 == 0:
        print (f"El nùmero {cont} es par")
    cont+=1    
    
print("//////////////////////////////////////////////////////////")    
#Uso del break, el ciclo para cuando llega a 4
contando=1
 
while contando <=10:
    if contando==5:
        break
    print("avanzo hasta el ",contando)
    
    contando+=1
    
print("/////////////////////////////////////////////////////////")   
#uso del continue 

con=1

while con <=10:
    con+=1  
    if con %2 == 0:
        print("El nùmero es par: ",con)
        continue  
                               
    print("El nùmero es impar: ",con)
    
print("/////////////////////////////////////////////////")    
#Uso del for con rango, imprime del 1 al 10
for i in range(10):
    print(i)
    
    
#uso del for con rangos, imprime del 5 al 10
print("/////////////////////////////////////////////////")    

for i in range(5,11):
    print(i)   
    
#Multiples rangos, como imprimir numeros de atras hacia adelante
#Imprime los números del 10 al 1 
print("Vamos a imprimir los número del 10 al 1 ")
for i in range(10, 0, -1):
    print(i)    
    
     
    
    
    
    



    
      
    



    
         
    
    
    
    
    
    