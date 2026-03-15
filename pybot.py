import subprocess

subprocess.run('cls',shell=True)

asistente_nombre="PyBot"
print(f"--- {asistente_nombre} Conectado ---")

#Interacción básica
usuario_nombre= input("Hola, soy tu asistente 🤖\n¿Cuál es tu nombre? ")
print(f"Mucho gusto, {usuario_nombre}.\n🤖¡Que buen nombre!")

#Un poco de lógica de cálculo
anio_nacimiento = input("¿En que año naciste? ")
edad=2026 - int(anio_nacimiento)

#Repuesta dinámica
print(f"Tienes {edad} años.\n🤖¡Es una gran edad para aprender Python!")

#Despedida personalizada
print(f"Un placer ayudarte hoy, {usuario_nombre} 🤖\n¡Cerrando sesión!")
