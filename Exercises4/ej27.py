from moduloimagen import leerImagen, mostrarImagen

def aplicar_filtro_negativo(imagen):
    imagen_filtro=imagen[:]
    for i in range(len(imagen_filtro)):
        for j in range(len(imagen_filtro[i])):
            imagen_filtro[i][j]=(255-imagen_filtro[i][j])
    return imagen_filtro


def main():
    nombreFichero = input("Introduce el nombre de la imagen: ")
    matriz = leerImagen(nombreFichero)
    mostrarImagen(aplicar_filtro_negativo(matriz))

main()