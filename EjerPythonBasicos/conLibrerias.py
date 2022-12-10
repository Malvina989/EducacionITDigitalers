import time, random
# Contador temporizador
# Hacer un script contador de 0 hasta 10, que vaya mostrando los números segundo a segundo

for i in range(0, 11):
    print(i)
    time.sleep(1)

# Dado
# Generar un programa de consola que tenga un menú y permita generar números aleatorios
# entre 1 y 6, como si fuera un dado. Menú 1. Tirar dado. 2. Salir


while True:
    opcion = int(input("1- Tirar dados\n2- Salir\n"))
    if opcion == 1:
        dado = random.randint(1, 6)
        print(f"Obtuviste:\n{dado}")
    elif opcion == 2:
        print("Gracias por jugar con nosotros")
        break
    else:
        print("Opción no válida")