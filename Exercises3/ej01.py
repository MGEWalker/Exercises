from math import pi
def área_círculo (x):
    return (pi*(x**2))
def longitud_circunferencia (x):
    return (2*pi*x)

area= float(input("Introduce el radio: "))
print(f'Área: {área_círculo(area): .2f}')
print(f'Longitud: {longitud_circunferencia(area): .2f}')