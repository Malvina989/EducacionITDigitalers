# Al ejercicio que está en Laboratorio adicional 2, el de generar un número aleatorio de 1 al 6
# simulando arrojar un dado, ahora debemos pasarlo a una aplicación de escritorio.

import tkinter as tk
from tkinter import ttk
import random

def tirar():
    valor.delete(0, tk.END)
    dado = random.randint(1, 6)
    valor.insert(0, dado)


ventana = tk.Tk()
ventana.title("Juego Dados")
ventana.config(width=300, height=300)

tirarDado = ttk.Button(text="Tirar Dado", command=tirar)
tirarDado.place(x=100, y= 50, width=100, height=100)

etiqueta = tk.Label(text="Valor: ")
etiqueta.place(x=130, y=170)
valor = tk.Entry()
valor.place(x=100, y=190, width=100, height=35)


ventana.mainloop()