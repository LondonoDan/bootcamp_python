
#tuplas
tupla=(1,2,3,4,5,6,7)

print(tupla)


#encontrar una palabra o un dato dentro de una tupla

TUPLA=("hola","que mas","chao")

for palabra in TUPLA:
    if palabra=="que mas": 
        print("He encontrado la palabra que mas")
        #el break se pone para que rompa el ciclo y no se siga hiterando
        break
    
    
#no se encuentra la palabra

if "ey" not in TUPLA:
    print("No se encuentra la palabra en la tupla")
            