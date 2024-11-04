n = int(input("Introduce un número entero: "))
print(f"Los números abundantes menores que {n} son:", end=' ')
for num in range(1, n):
    suma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            suma_divisores += i
    if suma_divisores > num:
        print(num, end=' ')
print()