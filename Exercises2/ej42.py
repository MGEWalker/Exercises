n = int(input("Introduce un número entero: "))
contador = 0
num = 12
print(f"Los {n} primeros números abundantes son:", end=' ')
while contador < n:
    suma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            suma_divisores += i
    if suma_divisores > num:
        print(num, end=' ')
        contador += 1
    num += 1
print()