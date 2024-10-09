class Alumno:
    nombre = "Daniela"
    
    
    
    def Nota(self): 
        nota= 4.5
    
        if nota >= 3:
            print("El alumno 👨👩 aprobo la materia con una nota de ",nota)
        
        else:
            print("El alumno 👨👩 NO aprobo la materia con una nota de ",nota)
        
        
alumno1 = Alumno()
print("El nombre del alumn@ 👨👩 es: ",alumno1.nombre)
alumno1.Nota()        
            
    
    
    