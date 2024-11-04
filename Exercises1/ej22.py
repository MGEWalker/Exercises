import math
lado1=float(input("Introduce el primer lado: "))
lados1=float(input("Introduce el segundo lado: "))
angulo1=float(input("Introduce el ángulo (en radianes): "))
print("El área del triángulo es: " f'{((lado1*lados1)/2)*(math.sin(angulo1)): .2f}' )