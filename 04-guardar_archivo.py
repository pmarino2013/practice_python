#La instrucción with open(): Explicamos por qué es la forma segura de abrir archivos sin que se corrompan.

#Modos de apertura: * 'r' (leer)

#'w' (escribir/sobrescribir)

#'a' (agregar al final - append)

# with open("archivo/nota.txt","a") as archivo:
#     archivo.write("Esto es una nota nueva\n")

password="contraseña123"

password_user=input("Ingrese la contraseña de acceso: ")

if password==password_user:
    print("Acceso aprobado✅")
else: 
    print("Acceso denegado❌")


from datetime import datetime

fecha= datetime.now().strftime("%d-%m-%Y %H:%M")


def escribir_archivo():
    texto=input("Escribe una párrafo nuevo: ")
    with open("archivo/nota.txt","a") as archivo:
        archivo.write(f"{fecha} - {texto}\n")
    leerNota()
     
def leerNota():
    with open("archivo/nota.txt", "r") as archivo:
        print(archivo.read())

def reescribir_archivo():
    texto=input("Escribe una párrafo nuevo: ")
    with open("archivo/nota.txt","w") as archivo:
         archivo.write(f"\n{fecha} - {texto}")

escribir_archivo()
# reescribir_archivo()