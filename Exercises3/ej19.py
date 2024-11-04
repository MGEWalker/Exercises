permitidas = "qwertyuiopñlkjhgfdsazxcvbnméíóáúü"
print("Ve introduciendo palabras, o vacío para acabar...")
while True:
    cadena = input("Nueva palabra: ")
    if cadena == "":
        break
    novalid = False
    for char in cadena:
        if char.lower() not in permitidas:
            print(f"Contiene un carácter que no es del alfabeto castellano: '{char}'")
            novalid = True
            break
    if not novalid:
        print("Podría ser una palabra correcta")
print("¡Adiós!")
