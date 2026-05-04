
# usuario ={
#     "nombre":'Pablo',
#     "edad":43,
#     "rol":"ADMIN"

# }

# print(usuario["nombre"])

# El usuario ingresa los datos de un contacto.

# Python los guarda en un diccionario.

# Ese diccionario se añade a una lista de "Contactos".

# La lista entera se guarda en un archivo llamado agenda.json.
import json
import os
import subprocess

if os.name=='nt':
    subprocess.run('cls',shell=True)    

if os.path.exists("archivo/agenda.json"):
    with open("archivo/agenda.json","r") as archivo:
        agenda=json.load(archivo)
else:
    agenda=[]

while True:
    print("---AGENDA DE CONTACTOS---")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Salir")   

    opc= input("Elige una opción: ")

