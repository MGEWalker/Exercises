n = int(input("Introduce un número entero: "))
factorial = 1
i = 1
while factorial < n:
    i += 1
    factorial *= i
print(f"{n} es el factorial de {i}")
