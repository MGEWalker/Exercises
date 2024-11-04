a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
c = int(input("Introduce el tercer número: "))


mayor = a
menor1= b
menor2= c
if b > mayor:
    mayor = b
    menor1 = a
    menor2= c
if c > mayor:
    mayor = c
    menor1 = a
    menor2 = b
if (mayor**2)== (menor1**2+menor2**2) :
    print("Es rectángulo")
else :
    print("No es rectágulo")