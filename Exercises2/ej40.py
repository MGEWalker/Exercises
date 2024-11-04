n = int(input("Introduce un número entero: "))
contador = 0
num = 2
print(f"Los {n} primeros números primos son:", end=' ')
while contador < n:
    es_primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num, end=' ')
        contador += 1
    num += 1
print()