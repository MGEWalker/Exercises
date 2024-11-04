
def sumar_divisores_propios(x):
    suma_de_divisores=0
    for i in range (1, x):
        if x%i==0:
            suma_de_divisores +=i
    return suma_de_divisores

def es_abundante(y):
    if sumar_divisores_propios(y)>y:
        return True
    return False

num = int(input("Introduce un número entero: "))
print(f'Los números abundantes menores que {num} son:', end=' ' )
for i in range (1, num):
    if es_abundante(i)==True:
        print(i, end=' ')





