# ******************************  ETAPA 1  *********************************

# Una universidad desea crear un programa para contabilizar los cursos que tiene cada alumno.
# Para ello se debe realizar primero una aplicación de consola la cual debe solicitar el nombre de un
# alumno y la cantidad de cursos en la que se  encuentra inscripto.
# Estos dos valores deben almacenarse como una lista de dos elementos (el nombre y la cantidad
# de cursos como un número entero) en una lista  de alumnos.
# Una vez hecho esto, se debe hacer que el programa, al iniciar, pregunte cuál de las siguientes dos
# operaciones se debe realizar: ingresar un  alumno o ver la lista de alumnos ingresados. 
# Esto debe preguntarse infinitamente hasta que el usuario escriba “3”. 

# alumnos = []
# while True:
#     opcion = int(input("Ingrese la operación que desea ejecutar:\n 1- Ver la lista de alumnos\n 2- Añadir alumno\n 3- Salir"))
#     if opcion == 1:
#         print("La lista de alumnos es: ")
#         for alumn in alumnos:
#             print(f"Nombre: {alumn[0]} - Cursos:{alumn[1]}")
#     elif opcion == 2:
#         alumno = [input("Ingrese nombre de alumno"), int(input("Ingrese cantidad de cursos del alumno"))]
#         alumnos.append(alumno)
#         print(f"{alumno[0]} añadido con éxito")
#     elif opcion == 3:
#         break
#     else:
#         print("Seleccione opción válida")
# print("Gracias por utilizar el programa")

# *****************************  ETAPA 2  ***********************************

# La lista de alumnos que creamos en el módulo anterior ahora debe ser un diccionario, en donde
# las claves serán nombres de alumnos y los valores sus respectivas cantidades de cursos.
# Para esto se debe modificar el código de las opciones 1 y 2 (agregar un nuevo alumno y ver la
# lista de alumnos). La tercera opción será “Ver la cantidad de cursos
# de un alumno”. Deberá solicitar el nombre de un alumno e imprimir en pantalla el número de
# cursos que tiene asociados como clave. La cuarta opción es la de salir, como en la versión anterior.

alumnos = {}

while True:
    # Mostrar menú de opciones al usuario
    opcion = int(input("Ingrese la operación que desea ejecutar:\n 1- Ingresar alumno\n 2- Ver lista de alumnos\n 3- Ver cantidad de cursos de alumno\n 4- Salir"))

    # Opción 1: Ingresar alumno. Controlamos que la cantidad de cursos ingresada sea decimal
    if opcion == 1:
        nombre = input("Ingrese nombre de alumno: ")
        while True:
            cursos = input("Ingrese cantidad de cursos: ")
            if cursos.isdecimal() == True:
                alumnos[nombre] = cursos
                print(f"{nombre} ingresado correctamente\n")
                break
            
    # Opción 2: Ver la lista de todos los alumnos con sus correspondientes cursos
    elif opcion == 2:
        for nombres in alumnos:
            print(f"El alumno {nombres} está inscripto en {cursos} cursos")  

    # Opción 3: Mostrar cantidad de cursos de alumno determinado
    elif opcion == 3:
        nombre = input("Ingrese nombre del alumno: ") 
        if nombre in alumnos:
            print(f"La cantidad de cursos del alumno {nombre} es {alumnos[nombre]}\n\n") 

    # Opción 4: Salir del sistema
    elif opcion == 4:
        print("Gracias por utilizar el sistema.")
        break
    
    # Opción 5: mensaje en caso de que se seleccione opción no válida
    else:
        print("Seleccione opción válida")
