# Calculadora
# Crear una aplicación de escritorio con dos cajas de texto y un botón, de modo que al presionarlo
# se imprima en pantalla la suma de los dos números ingresados en las primeras.
# La disposición de los controles y el tamaño de la ventana son a elección del alumno.

import tkinter as tk
from tkinter import ttk, messagebox

# Función mensaje error para valores no numéricos
def error():
    messagebox.showerror(title="Error", message = "Ingrese solo números por favor")

# Función suma
def sumar():
    numero = num1.get()
    if numero.isdecimal():
        numero2 = num2.get()
        if numero2.isdecimal():
            suma = int(numero) + int(numero2)
            res.insert(0, suma)
        else:
            # messagebox.showerror(title="Error", message = "Ingrese solo números por favor")
            error()
            numero2 = num2.get()
    else:
        # messagebox.showerror(title="Error", message = "Ingrese solo números por favor")
        error()
        numero = num1.get()


    

# Interfaz de la app
ventana_ppal = tk.Tk()
ventana_ppal.title("Suma")
ventana_ppal.config(width=210, height=250)

num1 = ttk.Entry()
num1.place(x=20, y=30, width=50, height=50 )

boton = ttk.Button(text="+", command=sumar)
boton.place(x=80, y=40, width=50,  height=25)

num2 = ttk.Entry()
num2.place(x=140, y=30, width=50, height=50 )

res = ttk.Entry()
res.place(x=55, y=150, width=100, height=50 )

ventana_ppal.mainloop()