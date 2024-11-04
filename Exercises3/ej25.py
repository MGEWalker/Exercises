def contar_secuencias_dígitos(cadena):
    contador = 0
    en_digito = False
    for char in cadena:
        if char.isdigit():
            if not en_digito:
                contador += 1
                en_digito = True
        else:
            en_digito = False
    return contador

print("Ve introduciendo cadenas de caracteres, o vacío para acabar...")
while True:
    nueva_cadena = input("Nueva cadena: ")
    if nueva_cadena == "":
        break
    secuencias = contar_secuencias_dígitos(nueva_cadena)
    print(f"Secuencias de dígitos encontradas: {secuencias}")

print("¡Adiós!")