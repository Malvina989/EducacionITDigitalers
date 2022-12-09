# Se quiere buscar los múltiplos de 3 y de 5 en un rango que ingrese el usuario. Guardar los
# múltiplos en una lista. Se debe usar for asociado a un range

num1 = int(input("Ingrese num1"))
num2 = int(input("Ingrese num2"))
multiplos = []

for i in range(num1, num2+1):
    if i % 3 == 0 and i % 5 == 0:
        multiplos.append(i)

print(multiplos)

# Crear un programa que pida un número, verificar con el método isdecimal() que ese ingreso por input sea un número posible
# de convertir a entero y cpnvertirlo. En caso contrario volver a pedir el ingreso

ingreso = input("Ingrese numero")

while ingreso.isdecimal() == False:
    print("Ingrese número por favor")

ingreso = int(ingreso)
print(f"El número ingresado es: {ingreso}")

 


