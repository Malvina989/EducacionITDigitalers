# VALIDACIÓN
# Se preguntará el tipo de rol que desempeña una persona en una institución por una entrada del
# tipo input. Los valores posibles son “admin” o “profesor”.
# Luego si la persona es “admin” o “profesor”, se debería pedirla contraseña, siendo la única válida
# “1234” (la contraseña se toma como string). Si la contraseña ingresada es válida, se procederá a
# pedir el nombre de la persona, y si no es vacío, se lo saludará.
# Contemplar los casos donde no se cumple como corresponde y mostrar un mensaje en pantalla.


while True:
    rol = input("Ingrese si su rol es 'profesor' u 'admin'")
    if rol != "profesor" and rol != "admin":
        print("Usuario no válido")
    else:
        while True:
            contrasena = input("Ingrese su contraseña")
            if contrasena == "1234":
                name = input("Ingrese su nombre")
                while name == "" or name == " ":
                    print("Por favor ingrese nombre válido")
                    name = input("Ingrese su nombre")
                else:
                    print(f"Bienvenido {name}")
                    break
            else:
                print("Contraseña incorrecta")
        break  


  
       