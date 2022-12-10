# EJERCICIOS PRIMERAS CLASES.
# PYTHON CONDICIONALES, BUCLES, LISTAS, MATRICES

# 1) Tomás rindió 3 exámenes con notas: 10, 6 y 8. Mostrar promedio por pantalla

nota1 = 10
nota2 = 6
nota3 = 8
promedio = (nota1 + nota2 + nota3)/ 3
print(f"1) El promedio de Tomás es: , {promedio} \n\n")

# 2) Armar una frase con las 3 variables dadas y mostrarla por pantalla.
# Es obligatorio usar las 3 variables, pero también podés agregar palabras vos para generar una
# frase. No importa el orden que elijas para las variables.
# texto_uno = "potente", texto_dos = "sol", texto_tres = "triunfo"

texto1 = "potente"
texto2 = "sol"
texto3 = "trinfó"
print(f"2) El {texto1} {texto2} {texto3}\n\n")

# 3) Realizar un programa que tenga 2 variables, base = 10 y altura = 5, calcular el área de 
# un rectángulo y mostrar por pantalla.

base = 10 
altura = 5
area = base * altura
print(f"3) El área del rectángulo es: {area} metros\n\n")

# 4) Dadas 2 variables: a = 20 y b = 10, mostrar por
# pantalla su suma, resta, multiplicación y división.

a = 20
b = 10
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
print(f"4) La suma es: {suma} \nLa resta es: {resta} \nLa multiplicación es: {multiplicacion} \nLa división es: {division}\n\n")

# 5) Crear un programa que permita ingresar dos
# cadenas vía la consola y luego las compare,
# imprimiendo un mensaje en caso que sean
# iguales y otro en caso que sean diferentes.

print("5)")
cadena1 = input("Ingrese primera frase")
cadena2 = input("Ingrese segunda frase")
if cadena1 == cadena2:
    print("Ambas frases son idénticas")
else:
    print("Son dos frases diferentes")

# 6) Crear un programa que solicite el nombre de un alumno a través de la consola, y luego chequee
# que no esté vacío. En caso de estarlo, tiene que imprimir un mensaje
# de error; caso contrario, deberá imprimir un mensaje indicando que se ingresó correctamente.

print("6)")
nombre = input("Ingrese su nombre")
if nombre == "" or nombre == " ":
    print("ERROR")
else:
    print(f"Ha ingresado correctamente. Bienvenido {nombre}")

# 7) Pedir la edad por teclado y comparar si es mayor o menor de edad. No olvidar de que para
# poder comparar el ingreso debe ser convertido a int, ya que el usuario ingresa un número entero.

edad = int(input("Ingrese edad"))
if edad >= 18:
    print(f"{edad} es sufuciente para ir a la cárcel")
else:
    print("Sos impune\n\n")

# 8) Con un bucle while incrementar una variable entera de uno en uno (desde 0 a 10 sin incluir).
# Mostrar por pantalla el resultado por vuelta.

print("8)")
bandera = 1
while bandera < 10:
    print(bandera)
    bandera += 1

# 9) Pedir por teclado el nombre de usuario, si está vacío, volver a pedirlo hasta que se ingrese
# un nombre. Luego, saludar al usuario. 

nombre = input("Ingrese su nombre")
while nombre == "" or nombre == " ":
    nombre = input("Por favor ingrese su nombre")
print(f"Buenas, buenas {nombre}\n\n")

# 10)Lista de nombres. Se tiene la siguiente lista de nombres: nombres = ["Susana","Alejandro","Roberto"]
# Insertar entre Alejandro y Roberto a Paula. Y luego agregar al final a Silvina.
# Para finalizar, hay que recorrer la lista y mostrar a todos los nombres por pantalla.
print("10)")
nombres = ["Susana","Alejandro","Roberto"]
nombres.insert(2, "Paula")
nombres.append("Silvina")
for nombre in nombres:
    print(nombre)

# Se tiene una lista de nombres y se desea recorrer con un bucle for y con while.
# nombres = ["Agustina","Marisa","Juan","Osvaldo"]

lista =  ["Agustina","Marisa","Juan","Osvaldo"]
for elemento in lista:
    print(elemento)

indice = 0
while indice < len(lista):
    print(lista[indice])
    indice +=1

# Crear un programa que solicite una fila y una columna e imprima en pantalla el número en
# esa posición según la siguiente matriz: matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
# El programa debe chequear que la fila y la columna tengan valores válidos. 

matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
fila = int(input("Ingrese posición de la fila que desea acceder"))
columna = int(input("Ingrese posición de la columna que desea acceder"))

if fila < len(matriz):
	if columna < len(matriz[fila]):
		print(matriz[fila][columna])
	else:
		print("Columna fuera de rango")
else:
	print("Fila fuera de rango")


