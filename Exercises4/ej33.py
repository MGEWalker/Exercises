from moduloimagen import leerImagen, mostrarImagen

def nueva_matriz(filas, columnas, num):
    matriz = []
    for i in range(filas):
        fila = [num] * columnas
        matriz.append(fila)
    return matriz


def girada_izquierda(imagen):
    filas = len(imagen)
    columnas = len(imagen[0])
    matriz_resultado = nueva_matriz(columnas, filas, 0)
    for i in range(filas):
        for j in range(columnas):
            matriz_resultado[columnas - 1 - j][i] = imagen[i][j]

    return matriz_resultado


def main():
    nombreFichero = input("Introduce el nombre de la imagen: ")
    matriz = leerImagen(nombreFichero)
    mostrarImagen(girada_izquierda(matriz))


main()
