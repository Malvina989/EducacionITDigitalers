# Escriba un programa que permita crear una lista de nombres.
# Para ello, el programa tiene que pedir un número y luego solicitar esa cantidad de nombres para
# crear la lista. Por último, el programa tiene que mostrar la lista creada. 

long = int(input("Ingrese cantidad de nombres a ingresar"))
lista = []
contador =  0

while contador < long:
    lista.append(input("Ingrese nombre"))
    contador += 1

print(lista)

# A partir de diagrama de flujo de cómo se hace para calcular un año bisiesto. La
# idea es llevar este algoritmo a código Python.

a = int(input("Ingrese año"))
if a % 400 == 0:
    print(f"{a} es año bisiesto")
elif a % 4 == 0 and a % 100 != 0:
        print(f"{a} es bisiesto")
else:
    print(f"{a} no es bisiesto")
