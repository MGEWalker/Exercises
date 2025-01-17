from moduloimagen import leerImagen, mostrarImagen

def promedio_entorno(imagen, num_fila, num_columna):
    suma_de_puntos=0
    for i in range(num_fila-1, num_fila+2):
        for j in range(num_columna-1, num_columna+2):
            suma_de_puntos+=imagen[i][j]
    return (suma_de_puntos/9)



def main():
    nombreFichero = input("Introduce el nombre de la imagen: ")
    matriz = leerImagen(nombreFichero)
    número_fila=int(input("Introduce un número de fila: "))
    número_columna=int(input("Introduce un número de columna: "))
    print(f"El promedio en el entorno del punto ({número_fila},{número_columna}) es {promedio_entorno(matriz, número_fila, número_columna): .2f}")


main()