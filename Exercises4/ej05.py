def leer_lista_enteros():
    print("Ve introduciendo números enteros, o una cadena vacía para acabar...")
    lista = []
    while True:
        entrada = input("Nuevo número: ")
        if entrada == "":
            break
        num = int(entrada)
        lista.append(num)
    return lista

def borrar_elemento(lista, pos):

    if 0 <= pos < len(lista):
        lista.pop(pos)
        return True
    else:
        return False


lista = leer_lista_enteros()


while len(lista)>=1:
    print(f"¿Qué posición debo eliminar de {lista}? ", end="")
    pos = int(input())
    if borrar_elemento(lista, pos)==False:
        print("Posición incorrecta")

print("La lista ha quedado vacía")


