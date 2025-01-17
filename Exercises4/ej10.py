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


def posición_menor(lista):
    menor = lista[0]
    posicion = 0
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            posicion = i
    return posicion


def intercambiar(lista, i, j):
    if i != j:
        temporal = lista[i]
        lista[i] = lista[j]
        lista[j] = temporal


def main():
    lista = leer_lista_enteros()
    print(f"Lista leída: {lista}")

    if lista:
        pos_menor = posición_menor(lista)
        if pos_menor != 0:
            intercambiar(lista, 0, pos_menor)
        print(f"Modificada: {lista}")
    else:
        print("Modificada: []")



main()

