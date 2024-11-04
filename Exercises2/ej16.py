
n = int(input("Introduce un número entero: "))
resultado = ""
for i in range(1, n + 1):
    resultado += str(i)
    if i < n:
        resultado += ", "
print(resultado)