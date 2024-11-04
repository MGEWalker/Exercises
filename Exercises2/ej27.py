num = float(input("Introduce un número: "))
contador = 0
suma = 0
while num >= 0:
    suma += num
    contador += 1
    num = float(input("Introduce otro número: "))

if contador > 0:
    print(f'Media: {suma / contador}')
else:
    print(f'No se han introducido datos')


