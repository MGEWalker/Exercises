def leer_lista_enteros():
    lista_enteros = []
    print("Ve introduciendo números enteros, o una cadena vacía para acabar...")

    while True:
        entrada = input("Nuevo número: ")
        if entrada == "":
            break
        numero = int(entrada)
        lista_enteros.append(numero)
    return lista_enteros


numeros = leer_lista_enteros()
cuadrados=[]
for n in numeros:
    resultado=n**2
    cuadrados.append(resultado)
#cuadrados = [n ** 2 for n in numeros]

print(f"Cuadrados de los números leídos: {cuadrados}")
print(f"Números leídos: {numeros}")
