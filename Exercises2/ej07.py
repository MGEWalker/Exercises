a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
c = int(input("Introduce el tercer número: "))


menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c
print("El menor es:", menor)


