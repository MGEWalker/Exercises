def leer_lista_enteros():
    print("Ve introduciendo números enteros, o una cadena vacía para acabar...")
    lista = []
    while True:
        entrada = input("Nuevo número: ")
        if entrada == "":
            break
        num = int(entrada)
        lista.append(num)
    return lista

lista = leer_lista_enteros()

print(f"Lista leída: {lista}")
print("Ve contestando con números enteros, o con una cadena vacía para acabar...")
while True:
    print("¿Qué suma he de buscar en dos posiciones consecutivas?", end=" ")
    valor_suma = input()
    if valor_suma == "":
        break
    valor_suma = int(valor_suma)
    for i in range(len(lista) - 1):  # Este ajuste evita que se salga del índice
        if lista[i] + lista[i+1] == valor_suma:
            print(f"{lista[i]} + {lista[i+1]} = {valor_suma}")

print("¡Adiós!")
