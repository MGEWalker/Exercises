
def evaluación_test(plantilla, respuestas):
    if len(plantilla)!=len(respuestas):
        return None
    correctas = 0
    falladas = 0
    contestless = 0
    for i in range(len(respuestas)):
        if respuestas[i] == plantilla[i]:
            correctas += 1
        elif respuestas[i] == "*":
            contestless += 1
        else:
            falladas += 1
    return [correctas, falladas, contestless]


def procesar_test():
    nombre_fichero = input("Introduce el nombre de un fichero de test: ")

    with open(nombre_fichero, 'r') as f:
        lineas = f.readlines()
        plantilla = lineas[0].strip()

        for linea in lineas[1:]:
            partes = linea.strip().split('#')
            dni = partes[0]
            respuestas = partes[1]

            resultados_ex=evaluación_test(plantilla, respuestas)
            nota_final = 10 * (resultados_ex[0] - resultados_ex[1]) / len(plantilla)
            if nota_final<0:
                nota_final=0
            print(f"El alumno con DNI {dni} ha obtenido una nota de {nota_final: .2f} puntos")



procesar_test()