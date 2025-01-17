def evaluación_test(plantilla, respuestas):
    
    correctas = 0
    incorrectas = 0
    no_contestadas = 0
    
    for i in range(len(plantilla)):
        if respuestas[i] == '*':
            no_contestadas += 1
        elif respuestas[i] == plantilla[i]:
            correctas += 1
        else:
            incorrectas += 1
    
    return [correctas, incorrectas, no_contestadas]



def main():
    plantilla = input("Introduce la plantilla de respuestas correctas: ")
    
    alumnos_corregidos = 0
    print("Ve introduciendo respuestas de alumnos, o vacío para acabar...")
    while True:
        respuestas = input("Nuevas respuestas: ")
        
        if respuestas == "":
            break
        
        if len(respuestas) != len(plantilla):
            print(f"La cadena introducida es de longitud {len(respuestas)} (se esperaba {len(plantilla)})")
        else:
            # Llamamos a la función de evaluación
            resultados = evaluación_test(plantilla, respuestas)
            correctas, incorrectas, no_contestadas = resultados
            print(f"Resultados: {correctas} BIEN; {incorrectas} MAL; {no_contestadas} NS/NC")
            alumnos_corregidos += 1
    
    print(f"Alumnos corregidos: {alumnos_corregidos}")


main()
