from modulomatrices import leerMatrizEnteros

def sumar_fila(matriz, num_fila):
    suma_fila=0
    for i in range(len(matriz[num_fila])):
        suma_fila+=matriz[num_fila][i]
    return suma_fila


def main():
    nombreFichero = input("Introduce el nombre de un fichero: ")
    matriz1 = leerMatrizEnteros(nombreFichero)
    for i in range(len(matriz1)):
        print(f"La suma de los elementos en la fila {i} es {sumar_fila(matriz1, i)}")

main()