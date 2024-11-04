
def limpiar_cadena(cadena):
    return cadena.strip('- ')

cadena_original = input("Introduce una cadena de caracteres: ")

cadena_limpia = limpiar_cadena(cadena_original)
print(f"Cadena limpiada: =>{cadena_limpia}<=\nCadena original: =>{cadena_original}<= ")
