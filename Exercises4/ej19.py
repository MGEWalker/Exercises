from modulomatrices import leerMatrizEnteros

def sumar_elementos(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
    return suma


def main():
    nombreFichero = input("Introduce el nombre de un fichero: ")
    matriz1 = leerMatrizEnteros(nombreFichero)
    print(f"La suma de todos los elementos en la matriz es {sumar_elementos(matriz1)}")

main()