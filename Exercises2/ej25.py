n = int(input('Introduce un número entero: '))

contador =0
for i in range(1, n + 1):
    if n % i == 0:
        contador += i
print(f'La suma de los divisores de {n} es {contador}')
