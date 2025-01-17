from modulomatrices import leerMatrizEnteros

def sumar_encima_diagonal(matriz):
    if len(matriz) != len(matriz[0]):
        return None
    sumar_encima=0
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz[i])):
            sumar_encima += matriz[i][j]

    return sumar_encima

def main():
    nombreFichero = input("Introduce el nombre de un fichero: ")
    matriz1 = leerMatrizEnteros(nombreFichero)
    if sumar_encima_diagonal(matriz1) is None:
        print("Error. Se requiere una matriz cuadrada")
    else:
        print(f"La suma de los elementos por encima de la diagonal principal es {sumar_encima_diagonal(matriz1)}")

main()