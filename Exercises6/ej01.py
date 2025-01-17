def es_dígito(dígito):
    return dígito in "0123456789"

def es_carácter(carácter):
    return carácter.lower() in "qwertyuiopasdfghjklzxcvbnm"

def contar_digitos_letras(fichero):
    with open(fichero, 'r') as archivo:
        num_digitos = 0
        num_letras = 0

        for linea in archivo:
            for caracter in linea:
                if es_dígito(caracter):
                    num_digitos += 1
                elif es_carácter(caracter):
                    num_letras += 1
    print(f"Dígitos decimales: {num_digitos}")
    print(f"Letras del inglés: {num_letras}")

def main():
    nombre_fichero = input("Introduce el nombre de un fichero: ")
    contar_digitos_letras(nombre_fichero)

main()