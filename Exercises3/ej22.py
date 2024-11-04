def corregir_examen(plantilla):
    num_alumnos = 0

    while True:
        respuestas = input("Nuevas respuestas: ")

        if respuestas == "":
            break
        if len(respuestas) != len(plantilla):
            print(f"La cadena introducida es de longitud {len(respuestas)} (se esperaba {len(plantilla)})")
            continue

        bien = mal = ns_nc = 0
        for i in range(len(plantilla)):
            if respuestas[i] == '*':
                ns_nc += 1
            elif respuestas[i] == plantilla[i]:
                bien += 1
            else:
                mal += 1
        print(f"Resultados: {bien} BIEN; {mal} MAL; {ns_nc} NS/NC")
        num_alumnos += 1
    print(f"Alumnos corregidos: {num_alumnos}")



plantilla_respuestas = input("Introduce la plantilla de respuestas correctas: ")
print("Ve introduciendo respuestas de alumnos, o vacío para acabar...")
corregir_examen(plantilla_respuestas)
