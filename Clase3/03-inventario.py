
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
opcion=""

def agregar_inventario():
    producto=input("Agrega el nombre del producto: ")
    if len(producto)>0:
        stock.append(producto)
        return "Producto agregado al inventario!🎉"

def ver_inventario():
    if len(stock)>0: 
        print("Listado de inventario")
        for producto in stock:
            print(f"📌{producto}")
    else:
        print("No hay productos disponibles❕")



def mostrar_menu():
    print("---INVENTARIO DE PRODUCTOS---")
    print("1. Agregar producto")
    print("2. Ver inventario")
    print("3. Salir")

while continuar:
    mostrar_menu()
    opcion=input("Elige una opción: ")
    if opcion=="1":
       limpiar_consola()
       print(agregar_inventario())
    elif opcion=="2":
        limpiar_consola()
        ver_inventario()
    elif opcion=="3":
        limpiar_consola()
        print("Hasta luego!👋")
        continuar=False
    else:
        print("La opción elegida no existe ❌")


