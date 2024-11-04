def leer_entero_mayor_que (x):
    candidato=int(input(f"Introduce un entero mayor que {x}: "))
    while candidato<=x:
        candidato=int(input(f"Esperaba entero mayor que {x} y {candidato} no lo es. Dame otro: "))
    return candidato

def contar_divisores(x):
    contador_divisores=0
    for i in range (1, x+1):
        if x%i==0:
            contador_divisores+=1
    return contador_divisores

def es_primo(x):
    if contar_divisores(x)==2:
        return True
    return False

num1= leer_entero_mayor_que(0)
num2= leer_entero_mayor_que(num1)
print(f"Voy a buscar primos entre {num1} y {num2}...")
print("Encontrados: ", end=" ")
ninguno=0
for i in range (num1, num2+1):
    if es_primo(i):
        print(i, end=" ")
        ninguno+=1
if ninguno==0:
    print("ninguno")