
lineas = []
print("Ve introduciendo cadenas de caracteres, o vacío para acabar...")
while True:
    cadena = input("Nueva cadena: ")
    if cadena == "":
        break
    lineas.append(cadena)

print("Cadenas leídas:")
for linea in lineas:
    print(f"Cadena de longitud {len(linea)}: =>{linea}<= ")



