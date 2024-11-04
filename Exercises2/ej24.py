n = int(input('Introduce un número entero: '))

contador_divisores =0
for i in range(1, n + 1):
    if n % i == 0:
        contador_divisores +=1

# Muestra el resultado
print(f"El número {n} tiene {contador_divisores} divisores")



