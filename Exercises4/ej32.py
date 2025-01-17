from moduloimagen import leerImagen, mostrarImagen


def promedio_entorno(imagen, num_fila, num_columna):
    suma_de_puntos=0
    for i in range(num_fila-1, num_fila+2):
        for j in range(num_columna-1, num_columna+2):
            suma_de_puntos+=imagen[i][j]
    return (suma_de_puntos/9)

def nueva_matriz(filas, columnas, num):
    matriz = []
    for i in range(filas):
        fila = [num] * columnas
        matriz.append(fila)
    return matriz


def difuminada(imagen, num):
    filas = len(imagen)
    columnas = len(imagen[0])
    matriz_resultado = nueva_matriz(filas, columnas, 0)

    for i in range(filas):
        for j in range(columnas):
            if i == 0 or i == filas - 1 or j == 0 or j == columnas - 1:
                matriz_resultado[i][j] = num
            else:
                promedio = promedio_entorno(imagen, i, j)
                matriz_resultado[i][j] = round(promedio)

    return matriz_resultado


def main():
    nombreFichero = input("Introduce el nombre de la imagen: ")
    matriz = leerImagen(nombreFichero)
    valor_borde=int(input("Introduce el valor del borde: "))
    mostrarImagen(difuminada(matriz, valor_borde))

main()