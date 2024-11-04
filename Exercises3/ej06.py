
def contar_divisores(x):

    contador_divisores =0
    for i in range(1, x + 1):
        if x % i == 0:
            contador_divisores +=1
    return contador_divisores

n = int(input('Introduce un número entero: '))
print(f'El número {n} tiene {contar_divisores(n)} divisores')

