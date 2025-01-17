from moduloimagen import leerImagen, mostrarImagen


def nueva_matriz(filas, columnas, valor_inicial):
    matriz = []
    for i in range(filas):
        fila = [valor_inicial] * columnas
        matriz.append(fila)
    return matriz


def binarizada(imagen, umbral):
    matriz_binarizada=nueva_matriz(len(imagen), len(imagen[0]), 0)
    for i in range(len(imagen)):
        for j in range(len(imagen[i])):
            if imagen[i][j]>umbral:
                matriz_binarizada[i][j]=255
    return matriz_binarizada


def main():
    nombreFichero = input("Introduce el nombre de la imagen: ")
    matriz = leerImagen(nombreFichero)
    num_umbral=int(input("Introduce el umbral: "))
    mostrarImagen(binarizada(matriz, num_umbral))

main()