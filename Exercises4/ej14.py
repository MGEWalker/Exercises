
def leer_alturas():
    lista_de_alturas = []
    print("Ve introduciendo alturas sobre el nivel del mar, o una cadena vacía para acabar...")
    Kilómetro_num = 0
    while True:
        nueva_altura = input(f"Altura en metros en el punto kilométrico {Kilómetro_num}: ")
        if nueva_altura == "":
            break
        lista_de_alturas.append(int(nueva_altura))
        Kilómetro_num += 1
    return lista_de_alturas


def calcular_desniveles(lista_de_alturas):
    lista_de_desniveles = []
    for i in range(len(lista_de_alturas) - 1):
        desnivel = lista_de_alturas[i+1] - lista_de_alturas[i]
        lista_de_desniveles.append(desnivel)
    return lista_de_desniveles


def posición_máximo(lista_de_desniveles):
   maximo = -float('inf')  
   indice_maximo = -1  
   for i in range(len(lista_de_desniveles)):
        if lista_de_desniveles[i] >= maximo: 
            maximo = lista_de_desniveles[i]
            if i>indice_maximo:
                indice_maximo = i
   return indice_maximo


def main():
    alturas = leer_alturas()
    if len(alturas)<=1:
        print("Recorrido no válido, con menos de dos puntos")
        return
    print(f"Lista de alturas: {alturas}")
    desniveles = calcular_desniveles(alturas)
    print(f"Lista de desniveles: {desniveles}")

    mayor_desnivel = posición_máximo(desniveles)
    
    if desniveles[mayor_desnivel] >0:  
        print(f"Kilómetro con mayor desnivel de subida: ")
        print(f"Entre los puntos kilométricos {mayor_desnivel} y {mayor_desnivel+1}")
        print(f"Desnivel de {desniveles[mayor_desnivel]} m")
    else:
        print("Ningún kilómetro es de subida")


main()
