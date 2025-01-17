
lineas = []
print("Ve introduciendo cadenas de caracteres, o vacío para acabar...")
while True:
    cadena = input("Nueva cadena: ")
    if cadena == "":
        break
    lineas.append(cadena)

print("Cadenas leídas (desde la última hasta la primera): ")
posición= len(lineas)-1
while posición > -1:
    linea= lineas[posición]
    print(f"Cadena de longitud {len(linea)}: =>{linea}<= ")
    posición-=1