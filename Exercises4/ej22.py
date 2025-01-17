from modulomatrices import leerMatrizEnteros

def sumar_diagonal(matriz):
    if len(matriz) != len(matriz[0]):
        return None
    suma_diagonal=0
    for i in range(len(matriz)):
        suma_diagonal+=matriz[i][i]
    return suma_diagonal


def main():
    nombreFichero = input("Introduce el nombre de un fichero: ")
    matriz1 = leerMatrizEnteros(nombreFichero)
    if sumar_diagonal(matriz1) is None:
        print("Error. Se requiere una matriz cuadrada")
    else:
        print(f"La suma de los elementos en la diagonal principal es {sumar_diagonal(matriz1)}")

main()