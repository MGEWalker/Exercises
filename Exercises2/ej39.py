n = int(input("Introduce un número entero: "))
print(f"Los números primos menores que {n} son:", end=' ')
for num in range(2, n):
    es_primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num, end=' ')
print()
