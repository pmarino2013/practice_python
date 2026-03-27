# 🛠️ Ejercicio de tarea (El desafío del "Barman")

# Crear un script que pregunte qué bebida quiere el cliente.
# Si elige "Cerveza", preguntar la edad. Si es menor de 18, denegar.
# Si elige "Jugo", servirlo sin preguntar la edad.
# Si elige cualquier otra cosa, decir "No tenemos esa bebida disponible".
import subprocess
subprocess.run('cls', shell=True)

print("---BARMAN VIRTUAL---")
print("Lista de bebidas virtuales")
print("1. Cerveza🍺")
print("2. Jugo🧃")
bebida_elegida=input("Elige una de las opciones disponibles: ")

if bebida_elegida=="1":
    validar_edad=input("Eres menor de 18 años?🤔 (si, no) ")
    if validar_edad=="si":
        print("No puedes beber alcohol 🫤")
    else:
        print("Sirviendo: 🍺")
elif bebida_elegida=="2":
    print("Sirviendo: 🧃")
else:
    print("No tenemos esa bebida 😔")