import math
lado2=float(input("Introduce el primer lado: "))
lados2=float(input("Introduce el segundo lado: "))
angulo2=float(input("Introduce el ángulo (en grados): "))
print("El área del triángulo es:", f'{((lado2*lados2)/2)*(math.sin((math.pi*angulo2)/180)): .2f}' )
