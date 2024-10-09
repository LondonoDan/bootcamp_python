class Vehiculo:
    color = "Verde  🟢 🚜 "
    ruedas = 4
    puertas = 2
    
    
class Coche(Vehiculo):
    velocidad = True
    cilindrada = False
    
    
CarroTractor = Coche()
print("El color del vehiculo tractor es: "+Coche.color)
print("la cantidad de ruedas son de: " ,Coche.ruedas)  
print("La cantidad de puertas del vehiculo es de: ",Coche.puertas)      
print("La velocidad es de: " ,Coche.velocidad)
print("El cilindraje del vehiculo es de: ",Coche.cilindrada)

    