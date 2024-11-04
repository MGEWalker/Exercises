def es_sufijo(cadena_a, cadena_b):
    longitud_a = 0
    longitud_b = 0

    while cadena_a[longitud_a:]:
        longitud_a += 1
    while cadena_b[longitud_b:]:
        longitud_b += 1
    if longitud_b == 0:
        return True
    if longitud_b > longitud_a:
        return False

    for i in range(longitud_b):
        if cadena_a[longitud_a - longitud_b + i] != cadena_b[i]:
            return False

    return True

cadena_a = input("Introduce una cadena de caracteres A: ")
cadena_b = input("Introduce una cadena de caracteres B: ")

if es_sufijo(cadena_a, cadena_b):
    print("B es sufijo de A")
else:
    print("B no es sufijo de A")
