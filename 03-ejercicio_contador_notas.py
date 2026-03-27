

print("---CONTADOR DE NOTAS---")

cantidad=5
suma=0
notas=[]

while cantidad:
    nota=(input('Ingrese la nota: '))
    if nota!="" and int(nota)>=0:
        notas.append(nota)
        cantidad=cantidad-1
    else:
        print("Debe ingresar una nota")
for nota in notas:
    suma=suma+int(nota)
print(f"El promedio de las notas ingresadas es: {suma/5}")