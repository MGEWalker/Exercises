from modulomatrices import leerMatrizEnteros

def sumar_columna(matriz, num_columna):
    suma_columna=0
    for i in range(len(matriz)):
        suma_columna+=matriz[i][num_columna]
    return suma_columna


def main():
    nombreFichero = input("Introduce el nombre de un fichero: ")
    matriz1 = leerMatrizEnteros(nombreFichero)
    for i in range(len(matriz1[0])):
        print(f"La suma de los elementos en la columna {i} es {sumar_columna(matriz1, i)}")

main()