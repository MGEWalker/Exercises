numero = int(input("Introduce un número entero: "))
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
if es_primo(numero):
    print(f"Es primo")
else:
    print(f"No es primo")

