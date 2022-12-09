# Una universidad desea crear un programa para contabilizar los cursos que tiene cada alumno.
# Para ello se debe realizar primero una aplicación de escritorio la cual debe solicitar el nombre de un
# alumno y la cantidad de cursos en la que se  encuentra inscripto.
# La lista de alumnos debe ser un diccionario, en donde
# las claves serán nombres de alumnos y los valores sus respectivas cantidades de cursos.
# Para esto las opciones 1 y 2 (agregar un nuevo alumno y ver la
# lista de alumnos). La tercera opción será “Ver la cantidad de cursos
# de un alumno”. Deberá solicitar el nombre de un alumno e imprimir en pantalla el número de
# cursos que tiene asociados como clave. La cuarta opción es la de salir.

import tkinter as tk
from tkinter import ttk, messagebox

# Declaro diccionario
alumnos = {}

# Ver lista de todos los alumnos y cursos
def verLista():
    salida.insert(0, alumnos)
        
# Agregar alumnos
def agregar(): 
    
    while True:
        alumno = nombre.get()
        cantidad = cursos.get()
        if cantidad.isdecimal() == True:
            alumnos[alumno] = cantidad
            print(f"{alumno} ingresado correctamente\n")
            messagebox.showinfo(title="Correcto", message = "Alumno ingresado correctamente")
            break
        else:
            messagebox.showerror(title="Error", message = "La cantidad debe ser numérica")
            cursos.delete(0, tk.END)
            break
            

# Ver cantidad de cursos de determinado alumno
def cantCursos():
    alumn = nombre.get()
    cursos.insert(0, alumnos[alumn])

# Interfaz de la app

ventana_ppal = tk.Tk()
ventana_ppal.title("Cursos por alumno")
ventana_ppal.config(width=600, height=280)

lista = ttk.Button(text="Ver lista de alumnos", command=verLista)
lista.place(x=20, y=30, width=200,  height=25)
salida = ttk.Entry()
salida.place(x=250, y=30, width=300, height=40)

etiquetaNombre = tk.Label(text="Nombre del alumno: ")
etiquetaNombre.place(x=40, y=90, width=130, height=25)
nombre = ttk.Entry()
nombre.place(x=170, y=90, width=290, height=25 )

cursos = ttk.Entry()
cursos.place(x=170, y=130, width=290, height=25 )
etiquetaCursos = tk.Label(text="Cantidad de cursos: ")
etiquetaCursos.place(x=40, y=130, width=130, height=25)

agregarAlum = ttk.Button(text="Agregar alumno", command=agregar)
agregarAlum.place(x=190, y=180, width=100,  height=25)

verCursos = ttk.Button(text="Ver cursos", command=cantCursos)
verCursos.place(x=310, y=180, width=100,  height=25)



ventana_ppal.mainloop()