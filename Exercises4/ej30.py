from moduloimagen import leerImagen, mostrarImagen

def nueva_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = [0] * columnas
        matriz.append(fila)
    return matriz


def reflejar_vertical(imagen):
    matriz_resultado = nueva_matriz(len(imagen), len(imagen[0]))
    for i in range(len(imagen)):
        matriz_resultado[len(imagen)-i-1]=imagen[i]
    return matriz_resultado


def main():
    nombreFichero = input("Introduce el nombre de la imagen: ")
    matriz = leerImagen(nombreFichero)
    mostrarImagen(reflejar_vertical(matriz))

main()