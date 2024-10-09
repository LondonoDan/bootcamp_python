import tkinter
from tkinter import ttk

windows = tkinter.Tk() 
windows.columnconfigure(0, weight=1)
windows.columnconfigure(0, weight=3)
selecion= tkinter.IntVar()

pregunta = ttk.Label(windows, text="Cuando es 2 + 2?")
r1 = ttk.Radiobutton(windows, text="8", value=1,  variable = selecion)
r2 = ttk.Radiobutton(windows, text="4", value=2,  variable = selecion)
r3 = ttk.Radiobutton(windows, text="10", value=3,  variable = selecion)
r4 = ttk.Radiobutton(windows, text="1", value=4,  variable = selecion)
#los posicionamos o los mostramos sea con pack, grid o el que queramos
pregunta.grid(column=0, row=4, sticky= tkinter.W)
r1.grid(column=0, row=5, sticky= tkinter.W)
r2.grid(column=0, row=6, sticky= tkinter.W)
r3.grid(column=0, row=7, sticky= tkinter.W)
r4.grid(column=0, row=8, sticky= tkinter.W)

#boton reset
def reset():
    return selecion.set(0)

resetear =ttk.Button(windows, text="Reset", command=reset).grid(column=0, row=9)

windows.mainloop()