import math
n = int(input("Introduce un número entero: "))
max_divisores = 0
numero_maximo = 0

for num in range(1, n + 1):
    contador_divisores = 0

    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            contador_divisores += 1
            if i != num // i:
                contador_divisores += 1

    if contador_divisores > max_divisores:
        max_divisores = contador_divisores
        numero_maximo = num
    elif contador_divisores == max_divisores:
        numero_maximo = max(numero_maximo, num)

print(f"El número con más divisores es {numero_maximo} ({max_divisores} divisores)")