def es_letra_castellana(caracter):
    permitidas = "qwertyuiopñlkjhgfdsazxcvbnméíóáúü"
    return caracter.lower() in permitidas
def primer_no_castellano(cadena):
    for char in cadena:
        if not es_letra_castellana(char):
            return char
    return None

print("Ve introduciendo palabras, o vacío para acabar...")
while True:
    cadena = input("Nueva palabra: ")
    if cadena == "":
        break
    caracter_no_castellano = primer_no_castellano(cadena)
    if caracter_no_castellano is None:
        print("Podría ser una palabra correcta")
    else:
        print(f"Contiene un carácter que no es del alfabeto castellano: '{caracter_no_castellano}'")

print("¡Adiós!")
