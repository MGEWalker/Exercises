num = float(input("Introduce un número: "))
if num < 0:
    print("No se han introducido datos")
else:
    suma = num
    contador = 1
    minimo = num
    maximo = num
    while True:
        num = float(input("Introduce otro número: "))
        if num < 0:
            break
        suma += num
        contador += 1
        if num < minimo:
            minimo = num
        if num > maximo:
            maximo = num
    media = suma / contador
    print(f"Media: {media}")
    print(f"Mínimo: {minimo}")
    print(f"Máximo: {maximo}")