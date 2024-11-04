posibles="0123456789"
nodigit=0
cadena=input("Introduce una cadena de caracteres: ")

for i in range (0, len(cadena)):
        if cadena[i]  not in posibles:
            nodigit+=1
if nodigit==0:
    suma=0
    print("Todos los caracteres son dígitos")
    print(f"¿cuántos dígitos? {len(cadena)}")
    print(f"¿Suma de dígitos?", end=" ")
    for i in range (0, len(cadena)):
        suma+=int(cadena [i])
    print(suma)
else:
    primernodigit=0
    incremento=0
    while str(primernodigit) in posibles:
        primernodigit=cadena[incremento]
        incremento+=1
    print(f"Primer \"no dígito\": '{cadena[incremento-1]}' en posición {incremento-1}")