from modulomatrices import leerMatrizEnteros

def sumar_debajo_diagonal(matriz):
    if len(matriz) != len(matriz[0]):
        return None
    sumar_debajo = 0
    for i in range(1, len(matriz)):
        for j in range(i):
            sumar_debajo += matriz[i][j]

    return sumar_debajo

def main():
    nombreFichero = input("Introduce el nombre de un fichero: ")
    matriz1 = leerMatrizEnteros(nombreFichero)
    if sumar_debajo_diagonal(matriz1) is None:
        print("Error. Se requiere una matriz cuadrada")
    else:
        print(f"La suma de los elementos por debajo de la diagonal principal es {sumar_debajo_diagonal(matriz1)}")

main()