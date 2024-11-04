a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))

if (a>0 and b>0) or (a<0 and b<0):
    print("Su producto es positivo")
elif a==0 or b==0:
    print("Su producto es nulo")
else:
    print("Su producto es negativo")