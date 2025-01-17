

def posición_menor(lista, inicio):
    menor_pos = inicio
    for i in range(inicio + 1, len(lista)):
        if lista[i] < lista[menor_pos]:
            menor_pos = i
    return menor_pos

def intercambiar(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        pos_menor = posición_menor(lista, i)
        if pos_menor != i:
            intercambiar(lista, i, pos_menor)


def procesar_DNI():
    nombre_fichero = input("Introduce el nombre de un fichero de test: ")

    with open(nombre_fichero, 'r') as f:
        lineas = f.readlines()

        listado_DNIs = []
        for linea in lineas[1:]:
            partes = linea.strip().split('#')
            dni = partes[0]
            listado_DNIs.append(dni)
        ordenar_lista(listado_DNIs)

        for dni in listado_DNIs:
            print(f"{dni}")

procesar_DNI()


