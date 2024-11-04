texto = input("Introduce un texto (vacío para acabar): ")
if texto=="":
    print("No se ha introducido ningún texto")
else:
    grande=""
    pequeña=texto
    if len(texto) >= len(grande):
        grande = texto
    if len(texto) <= len(pequeña):
        pequeña = texto
    while texto!="":
        if len(texto)>=len(grande):
            grande=texto
        if len(texto)<=len(pequeña):
            pequeña=texto
        texto = input("Introduce otro texto (vacío para acabar): ")
    print(f"Última cadena de mínima longitud, {len(pequeña)}: =>{pequeña}<=")
    print(f"Última cadena de máxima longitud, {len(grande)}: =>{grande}<=")
