
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
print(f'Los {num} primeros números abundantes son:', end=' ' )
max=0
candidato=0
while max<num:
    if es_abundante(candidato)==True:
        print(candidato, end=' ')
        max+=1
    candidato+=1
