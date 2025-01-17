def cadena_mas_larguirucha():
    nombre_fichero = input("Introduce el nombre de un fichero: ")
    cadena_más_larguirucha = ""

    with open(nombre_fichero, 'r') as f:
        lineas = f.readlines()
        for linea in lineas:
            partes = linea.strip().split()
            for cadena in partes:
                if len(cadena) > len(cadena_más_larguirucha):
                    cadena_más_larguirucha = cadena

    print(f"Su secuencia de caracteres sin espacios más larga es \"{cadena_más_larguirucha}\".")


cadena_mas_larguirucha()
