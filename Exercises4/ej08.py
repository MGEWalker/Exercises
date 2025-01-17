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

def borrar_elemento(lista, element):
    if element not in lista:
        return False
    lista[:] = [e for e in lista if e != element]
    return True




lista = leer_lista_enteros()

while len(lista)>=1:
    print(f"¿Qué número debo eliminar de {lista}? ", end="")
    elemento = int(input())
    if borrar_elemento(lista, elemento) is False:
        print("Número no encontrado")

print("La lista ha quedado vacía")