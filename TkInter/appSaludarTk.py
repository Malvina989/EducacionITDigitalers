# Crear pequeña app de escritorio para saludar usuarios, generando lista de 5 elementos, e imprimiendo mensajes de error en caso
# de ingresar cadena vacía o superar el número de saludos


import tkinter as tk
from tkinter import ttk, messagebox


def saludar():
    # Definimos saludos como global para poder acceder desde fuera de la función
    global saludos

    # Borro en cada saludo el saludo anterior
    salida.delete(0, tk.END)

    # Tomamos nombre qu ingrese usuario en entrada
    nombre = entrada.get()
    
    # Saludo
    if saludos < 5:
        # Si el nombre está vacío se envía mensaje de error
        if nombre == "" or nombre == " ":
            messagebox.showerror(title="Error", message = "Es de locos andar saludando al vacío")
        # De lo contrario se saluda, se inserta el saludo en la lista y se incrementa un saludo   
        else:
            salida.insert(0,  f"<<             ¡Hola {nombre}!             >>" )
            lista.insert(0, "=>  " + nombre)
            saludos +=1

    # Mensaje de error si se supera número de saludos
    else:
        messagebox.showerror(title="Demasiados", message = "No hay que abusar de la simpatía")
        ventana_ppal.destroy()
        
    
saludos = 0

# Interfaz de la aplicación
ventana_ppal = tk.Tk()
ventana_ppal.title("Programa clase 3")
ventana_ppal.config(width=300, height=340)

entrada = ttk.Entry()
entrada.place(x=20, y=30, width=170, height=25 )

boton = ttk.Button(text="¡Saludar!", command=saludar)
boton.place(x=200, y=30, width=80,  height=25)

salida = ttk.Entry()
salida.place(x=20, y=90, width=260, height=120)

lista = tk.Listbox()
lista.place(x=20, y=220, width=260, height=90)


ventana_ppal.mainloop()