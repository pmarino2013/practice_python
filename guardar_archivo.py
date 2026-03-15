#La instrucción with open(): Explicamos por qué es la forma segura de abrir archivos sin que se corrompan.

#Modos de apertura: * 'r' (leer)

#'w' (escribir/sobrescribir)

#'a' (agregar al final - append)

# with open("archivo/nota.txt","a") as archivo:
#     archivo.write("Esto es una nota nueva\n")

def escribir_archivo():
    texto=input("Escribe una párrafo nuevo: ")
    with open("archivo/nota.txt","a") as archivo:
        archivo.write(texto)

def reescribir_archivo():
    texto=input("Escribe una párrafo nuevo: ")
    with open("archivo/nota.txt","w") as archivo:
        archivo.write(texto)

# escribir_archivo()
reescribir_archivo()