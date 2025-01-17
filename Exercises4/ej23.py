from modulomatrices import leerMatrizEnteros

def producto_diagonal_secundaria(matriz):
    if len(matriz) != len(matriz[0]):
        return None
    producto_diagonal=1
    for i in range(len(matriz)):
        producto_diagonal*=matriz[i][-(i+1)]
    return producto_diagonal

def main():
    nombreFichero = input("Introduce el nombre de un fichero: ")
    matriz1 = leerMatrizEnteros(nombreFichero)
    if producto_diagonal_secundaria(matriz1) is None:
        print("Error. Se requiere una matriz cuadrada")
    else:
        print(f"El producto de los elementos en la diagonal secundaria es {producto_diagonal_secundaria(matriz1)}")

main()