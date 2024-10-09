import tkinter as tk


windows = tk.Tk()
windows.geometry("400x300")
windows.title("Pregunta")

items = {
    "Banano",
    "Manzana",
    "Pera",
    "sandia"
}

miLista = tk.Listbox(windows,width=50, selectmode=tk.EXTENDED)
miLista.insert(1, *items)
miLista.grid(column=1, row=0 )
miLista.insert(0, "¿Cual es tu fruta favorita?")
windows.mainloop()