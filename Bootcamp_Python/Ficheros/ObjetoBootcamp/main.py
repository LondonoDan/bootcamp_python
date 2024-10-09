import pickle
class vehiculo:
    encendido = True
    apagado= False
    placa = ""
    modelo = 0
    
    def __init__(self, placa,modelo):
        self.placa = placa
        self.modelo = modelo
        
    def getPlaca(self):
        return self.placa
                 
    
    
    def enciende(self):
        self.encendido = print("Encendido.... de color 💜")
        
    def apaga(self):
        self.apagado = print("Apagando...")
        
        
carro1=vehiculo("abc345", 2009)
carro1.enciende()
print(carro1.getPlaca)

#m = open("save.bin", 'wb')
#pickle.dump(carro1,m)
#m.close()

m= open("save.bin", 'rb')
nombre = pickle.load(m)
m.close()




print("la placa: ",nombre.getPlaca(), " es un modelo " , nombre.modelo)











        