

# usuario={
#     "nombre":"Alberto Perez",
#     "edad":56,
#     "area":"Mecánica"
# }

# print(usuario["nombre"])
import json
import os
import subprocess

contactos=[]

def limpiar_consola():
    if(os.name=="nt"):
        subprocess.run("cls",shell=True)
    else:
        subprocess.run("clear",shell=True)

if os.path.exists("archivo/agenda.json"):
    with open("archivo/agenda.json","r") as f:
        contactos=json.load(f)
        
limpiar_consola()

while True:
    print("\n--- AGENDA CLOUD 2.0 ---")
    print("1. Agregar | 2. Mostrar todos | 3. Salir")
    opcion=input("Selecciona: ")

    if opcion=="1":
        nuevo={
            "nombre":input("Nombre: "),
            "tel":input("Teléfono: "),
            "email":input("Email: ")
        }
        contactos.append(nuevo)

        #agregar al json
        with open("archivo/agenda.json","w") as f:
            json.dump(contactos,f,indent=4)
        print("✅ Guardado en la nube local")

    elif opcion=="2":
        limpiar_consola()
        if len(contactos)>0:
            print("--- LISTA DE CONTACTOS ---")
            for contacto in contactos:
               print(f"👤 {contacto["nombre"]} - 📞 {contacto["tel"]} - 📧 {contacto["email"]}")
        else:
            print("⚠️ No hay registros para mostar")
    elif opcion=="3":
        break
    else:
        print("Opción incorrecta❌")



