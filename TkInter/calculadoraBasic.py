import tkinter as tk
from tkinter import ttk, messagebox



# Función mensaje error para valores no numéricos
def error():
    messagebox.showerror(title="Error", message = "Ingrese solo números por favor")

# Funciones de suma, resta, multiplicación y división
def sumar():
    comprobar()
    suma = numero + numero2
    res.insert(0, suma)
    

def restar():
    comprobar()
    resta = numero - numero2
    res.insert(0, resta)

def multiplicar():
    comprobar()
    mult = numero * numero2
    res.insert(0, mult)

def dividir():
    comprobar()
    # No es posible dividir por cero
    try:
       division = numero / numero2
       res.insert(0, division)
    except ZeroDivisionError:
        messagebox.showerror(title="Error", message = "No es posible dividir por 0")

    

# Comprobar el ingreso de números
def comprobar():
    global numero
    global numero2
    res.delete(0, tk.END)
    numero = num1.get()
    if numero.isdecimal():
        numero2 = num2.get()
        if numero2.isdecimal():
            numero = int(numero) 
            numero2 = int(numero2)
            
        else:
            # messagebox.showerror(title="Error", message = "Ingrese solo números por favor")
            error()
            numero2 = num2.get()
    else:
        # messagebox.showerror(title="Error", message = "Ingrese solo números por favor")
        error()
        numero = num1.get()

def borrar():
    res.delete(0, tk.END)
    num1.delete(0, tk.END)
    num2.delete(0, tk.END)
    

def cerrar():
    ventana_ppal.destroy()    

# Interfaz de la app
ventana_ppal = tk.Tk()
ventana_ppal.title("Calculadora Básica")
ventana_ppal.config(width=210, height=280)

num1 = ttk.Entry()
num1.place(x=15, y=50, width=70, height=30 )

num2 = ttk.Entry()
num2.place(x=15, y=100, width=70, height=30)

boton = ttk.Button(text="+", command=sumar)
boton.place(x=100, y=40, width=50,  height=50)

boton = ttk.Button(text="-", command=restar)
boton.place(x=100, y=90, width=50,  height=50)

boton = ttk.Button(text="*", command=multiplicar)
boton.place(x=150, y=40, width=50,  height=50)

boton = ttk.Button(text="/", command=dividir)
boton.place(x=150, y=90, width=50,  height=50)

res = ttk.Entry()
res.place(x=35, y=150, width=150, height=30)

borrar = ttk.Button(text="<=", command=borrar)
borrar.place(x=65, y=190, width=90, height=30)

salir = ttk.Button(text="X", command=cerrar)
salir.place(x=65, y=230, width=90, height=30)

ventana_ppal.mainloop()





	 







  