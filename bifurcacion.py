# edad_usuario=int(input("Ingresa tu edad: "))

# if edad_usuario>=18:
#     print("Podés entrar al club.")
# elif edad_usuario >=13:
#     print("Podés entrar con un tutor")
# else:
#     print("No puedes entrar al club")

#------------------------------------------------------
import os
import subprocess

if os.name=='nt':
    subprocess.run('cls',shell=True)

password="admin123"
user="root"

print("---LOGIN DE SEGURIDAD---")
user_name=input("Usuario: ")
user_password=input("Contraseña: ")

if user_password==password and user_name==user:
    print(f"Acceso concedido. Cargando sistema...")

    print("1. Ver clima")
    print("2. Salir")

    opcion=input("Elige una opción: ")

    if opcion=="1":
        print("Hoy es un gran día para programar en Python🐍")
    elif opcion=="2":
        print("Hasta luego!👋")
    else:
        print("Error de sistema ❌")

else:
    print("Usuario o contraseña incorrecto")

