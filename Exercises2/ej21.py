n = int(input("Introduce un número entero: "))
for i in range(1, n):
    cuadrado = i ** 2
    if cuadrado < n:
        print(f"El cuadrado de {i} es {cuadrado}")
