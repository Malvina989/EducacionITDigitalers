# Sumar números con una función Crear una función que tome 2 números como
# argumentos y retorne el resultado.

def suma(num1, num2):
    resultado = num1 + num2
    return resultado

num1 = int(input("Ingrese num1"))
num2 = int(input("Ingrese num2"))

print(f"La suma de {num1} y {num2} es:", suma(num1, num2)) 


# Función para forzar el ingreso numérico.
# Crear una función que fuerce el ingreso de solo números. Debe recibir un número por argumento,
# y verificar que este sea un número posible de convertir a INT. En caso contrario, volver a pedir
# el ingreso dentro de la función. Deber de retornar el valor convertido a INT

def decimal(num): 
    while True:
        if num.isdecimal():
            return int(num)  
        else:
            num = input("Ingrese un número por favor") 
num = input("ingrese numero")


print(f"El número ingresado convertido a entero es: {decimal(num)}")


# Realiza una función llamada “area_rectangulo”  que reciba la base y la altura por argumento y
# que devuelva (retorne) el área del rectángulo.

def area(base, alt):
    area_rect = base * alt
    return area_rect

base = int(input("Ingrese base"))
alt = int(input("Ingrese altura"))

print(f"El área del rectángulo es: {area(base, alt)}")


# Generar un rango con una función. Crear una función rango (desde, hasta, intervalo)
# que retorne una lista de números, tal como la función incorporada range(), aunque según el
# intervalo especificado.(No puede usar la función range() para resolver este ejercicio)

def rango(desde, hasta, inter):
    lista = []
    while desde <= hasta:
        lista.append(desde)
        desde += inter
    return lista

desde = int(input("Ingrese desde qué número"))
hasta = int(input("Hasta qué número"))
inter = int(input("Ingrese intérvalo"))

print(rango(desde, hasta, inter))


# Escribir una función que sirva para multiplicar cada elemento de una lista numérica por un
# valor (ambos deben ser parámetros de función);  y devuelva la nueva lista con cada elemento en
# su respectiva posición, pero ya multiplicado. 

def mult_lista(lista, valor):
    nueva_list = []
    for i in lista:
        e = i * valor
        nueva_list.append(e)
    return nueva_list

list = [5, 3, 4]
val = 2
print(mult_lista(list, val))


# Hacer una función que reciba una lista con números enteros y devuelva en una “matriz”
# como primer elemento una lista con los números pares y como segunda lista los números
# impares de la lista recibida. Idea [pares , impares]

def separar(list_enteros):
    pares = []
    impares = []
    for i in list_enteros:
        if i % 2 == 0:
            pares.append(i)
        else: 
            impares.append(i)
    return [pares, impares]

list = [5, 3, 4, 8, 1, 5, 9]
print(separar(list))


