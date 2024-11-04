n = int(input('Introduce un número entero: '))
for i in range (1,n+1):
    factorial=1
    for k in range (1,i+1):
        factorial*=k
    print(f'{i}! = {factorial}')