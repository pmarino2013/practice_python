
import os
import subprocess

def limpiar_consola():

    if os.name=='nt':

        subprocess.run("cls",shell=True)
    else:
        subprocess.run("clear", shell=True)

limpiar_consola()
stock=[]
continuar=True

while continuar:
    print("---INVENTARIO DE PRODUCTOS---")
    print("1. Agregar producto")
    print("2. Ver inventario")
    print("3. Salir")
    opcion=input("Elige una opción: ")

    if opcion=="1":
        producto=input("Agrega el nombre del producto: ")
        if len(producto)>0:
            stock.append()
            print("Producto agregado al inventario!🎉")
    elif opcion=="2":
        if len(stock)>0: 
            print("Listado de inventario")
            for producto in stock:
                print(f"📌{producto}")
        else:
            print("No hay productos disponibles❕")
    elif opcion=="3":
        print("Hasta luego!👋")
        continuar=False
    else:
        print("La opción elegida no existe ❌")


