
pares = []
impares = []
print("Ve introduciendo números enteros positivos, o un número negativo para acabar...")

while True:
    numero = int(input("Nuevo número: "))
    if numero < 0:
        break
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números pares:", pares)
print("Números impares:", impares)

