
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

def repetidos_lista(lista):
    repetidos = []  
    ya_vistos = [] 
    
    for num in lista:
        if num not in ya_vistos:

            repeticiones = 0
            for elemento in lista:
                if elemento == num:
                    repeticiones += 1

            if repeticiones > 1:
                repetidos.append(num)
            
            ya_vistos.append(num)
    
    return repetidos


def suma_lista(lista):
    suma_de_num_cadena=0
    for num in lista:
        suma_de_num_cadena+=num

    return suma_de_num_cadena
    

def main():

    lista = leer_lista_enteros()
    lista_operaciones = lista[:]
    lista_de_repetidos=repetidos_lista(lista_operaciones)
    suma_lista_de_repetidos=suma_lista(lista_de_repetidos)

    print(f"Números leídos más de una vez (suman {suma_lista_de_repetidos}): {lista_de_repetidos}")
    print(f"Todos los números leídos: {lista}")




main()
