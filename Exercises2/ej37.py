n = int(input("Introduce un número entero: "))
a, b = 1, 1
if n <= 0:
    print("Por favor, introduce un número entero positivo.")
else:
    print(f"Los {n} primeros números de Fibonacci son:", end=' ')
    for i in range(n):
        if i == 0:
            print(a, end=' ')
        elif i == 1:
            print(b, end=' ')
        else:
            siguiente = a + b
            print(siguiente, end=' ')
            a, b = b, siguiente