num = float(input("Introduce un número: "))
if num < 0:
    print("No se han introducido datos")
else:
    maximo = num
    while True:
        num = float(input("Introduce otro número: "))
        if num < 0:
            break
        if num > maximo:
            maximo = num
    print(f"Máximo: {maximo}")