#interfaces de usuarios, nos permite interactuar con la misma, para ello vamos a trabajar con 
#tkinter, el cual se debe importar
#Hay varios modos de posicionar nuestros datos o objetos con .pack, .grid o .place (pisicionamiento exacto) 
#para usar columnconfigure, debemos importar la libreria from tkinter import ttk
#no podemos usas pack y ttk al mismo tiempor en una misma ventana para posicionar, ya que no va a dar

import tkinter
from tkinter import ttk

windows = tkinter.Tk() #se crea la ventana
#import pprint
#pprint.pprint(dir(windows)) #aca vamos a validar todos las funciones que tiene la interfaz tkinter

#posicionamiento de datos o botones
#saludo = tkinter.Label(windows, text="Hello everybody!!!!", bg="violet", fg="white") #creamos una etiqueta de saludo con un fon y un color de texto
#pack solo nos sirve para organizar arriba, abajo, izquierda o derecha
#saludo.pack(side="top") #esto nos permite mostrar el contenido de la etiqueta saludo, dentro de pack se le puede dar parametros, para posicionar el texto



#vamos a posicionar objetos con columnconfigure
#aca estamos indicando que se cree 2 columnas con 3 filas cada una
#ejemplo 
# (0,0) (1.0) (2,0) 
# (1,1) (1,1) (2,1)
windows.columnconfigure(0, weight=1)
windows.columnconfigure(0, weight=3)

#######################################################################################
#Vamos a crear una ventana que contenga 

#informacion = tkinter.Label(windows, text="vamos a crear una ventana con nombre y contraseña!!!!", bg="purple", fg="white")
#informacion.pack(side="top")
#ahora vamos a crear el boton de nombre 
user_name = ttk.Label(windows, text="ingrese el nombre: ")
user_name.grid(column=0, row=0, sticky= tkinter.W, padx=5, pady=5) # le estamos diciendo que se posicione en la columna 0 fila 0 y al oeste
#sticky, nos permite posicionar fijado a un sitio y que no se mueva, y permite pisicionar como si fuera una brujula norte, sur, oeste,
#y padx y pady el tamaño ancho y alto

#vamos a crear el campo para escribir adentro del mismo con Entry
userName_boton = ttk.Entry(windows)
userName_boton.grid(column=1, row=0, sticky= tkinter.E, padx=5, pady=5)

userName_contrasena= ttk.Label(windows, text="Ingrese la contraseña: ")
userName_contrasena.grid(column=0, row=1, sticky= tkinter.W, padx=5, pady=5)
contrasenaBoton = ttk.Entry(windows)
contrasenaBoton.grid(column=1, row=1, sticky= tkinter.E, padx=5, pady=5) 

#Boton de enviar
botonEnviar = ttk.Button(windows, text="Enviar")
botonEnviar.grid(column=1, row=3, sticky=tkinter.E)

#Vamos a crear botones de selecion, sea seleción con unica respuesta o multiple
#para crear una respuesta multiple debemos crear una variable de seleccionado diferente 
#La variable selecion= tkinter.StringVar() nos indica donde se esta guardando la respuesta, si ponemos todos los botones con esa variable es unida respuesta y si creamos varias es para multiples respuestas
#Ejemplo
#Creamos los textos o sus botones
selecion= tkinter.IntVar()

pregunta = ttk.Label(windows, text="Cuando es 2 + 2?")
r1 = ttk.Radiobutton(windows, text="8", value=1,  variable = selecion)
r2 = ttk.Radiobutton(windows, text="4", value=2,  variable = selecion)
r3 = ttk.Radiobutton(windows, text="10", value=3,  variable = selecion)

#los posicionamos o los mostramos sea con pack, grid o el que queramos
pregunta.grid(column=0, row=4, sticky= tkinter.W)
r1.grid(column=0, row=5, sticky= tkinter.W)
r2.grid(column=0, row=6, sticky= tkinter.W)
r3.grid(column=0, row=7, sticky= tkinter.W)

#boton enviar
botonEnviar = ttk.Button(windows, text="Enviar")
botonEnviar.grid(column=0, row=8, sticky=tkinter.E)


    

#funciones 
#creamos una que se cierre el programa cuando le demos click
def salir(event):
    print("adios")
    windows.quit()
    
def reset():
    return selecion.set(0)

resetear =ttk.Button(windows, text="Reset", command=reset).grid(column=0, row=9)
        
    
botonSalir = tkinter.Button(windows, text="Pinche aqui para salir") 
botonSalir.grid(column=0, row=10)   
botonSalir.bind('<Button-1>', salir) #Este comando nos permite que el programa finalice y muestre lo que le indicamos
    
    




 








#vamos a crear la ventana y que se quede abierta para interactuar, se debe crear todo lo de la interfaz
#antes de el mainloop, esta etiqueta siempre debe ir al final del programa
windows.mainloop()




