def todos_dígitos(cadena):
    for numi in cadena:
        if not es_digito(numi):
            return False
    return True

def es_digito(num):
    return num in "0123456789"

def mostrar_dígitos():
    nombre_fichero = input("Introduce el nombre de un fichero: ")

    with open(nombre_fichero, 'r') as f:
        lineas = f.readlines()

        for linea in lineas:
            partes = linea.strip().split()
            for palabra in partes:
                if todos_dígitos(palabra):
                    print(palabra)



mostrar_dígitos()
