
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


def posición_menor(lista, inicio):

    menor = lista[inicio]
    posicion = inicio
    for i in range(inicio + 1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            posicion = i
    return posicion


def intercambiar(lista, i, j):
    if i != j:
        temporal = lista[i]
        lista[i] = lista[j]
        lista[j] = temporal


def ordenar_lista(listain):
    if listain:
        for i in range(len(listain)):
            pos_menor = posición_menor(listain, i)
            intercambiar(listain, i, pos_menor)



def main():
    lista = leer_lista_enteros()
    print(f"Lista leída: {lista}")
    ordenar_lista(lista)
    if lista:
        print(f"Lista ordenada: {lista}")
    else:
        print("Lista ordenada: []")


main()