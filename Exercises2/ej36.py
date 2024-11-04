n = int(input("Introduce un número entero: "))
if n == 1 or n == 2:
    resultado= 1
fib1, fib2 = 1, 1
for i in range(3, n + 1):
    fib_actual = fib1 + fib2
    fib1, fib2 = fib2, fib_actual
resultado= fib2
print(f"Fibonacci({n}) = {resultado}")
