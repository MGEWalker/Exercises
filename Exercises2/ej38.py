n = int(input("Introduce un número entero: "))
a, b = 1, 1
i = 1
while a < n:
    a, b = b, a + b
    i += 1
if a == n:
    print(f"El número buscado es {i}")
else:
    print("No es un número de Fibonacci")