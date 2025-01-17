
def leer_candidaturas():
    candidatos_presentados=[]
    print("Ve introduciendo candidaturas, o vacío para acabar...")
    while True:
        candidatura=input("Nueva candidatura: ")

        if candidatura== "":
            break

        candidatos_presentados.append(candidatura)
    
    return candidatos_presentados


def votos_para_candidato(lista_de_candidatos):
    num_candidatos_presentados=len(lista_de_candidatos)
    votos_candidato=[]
    for i in range(0, num_candidatos_presentados):
        votos_para_el_candidato=int(input(f"Votos para {lista_de_candidatos[i]}: "))
        votos_candidato.append(votos_para_el_candidato)

    return votos_candidato
 
def total_de_votos(lista_de_los_votos):
    suma_de_votos=0
    for num in lista_de_los_votos:
        suma_de_votos+=num

    return int(suma_de_votos)

def mostar_porcentajes_de_votos(lista_de_candidatos, lista_de_votos, total_de_votos):
    for i in range(len(lista_de_candidatos)):
        print(f"{(lista_de_votos[i]/total_de_votos)*100:.2f}% de los votos a candidaturas para {lista_de_candidatos[i]}")



def main():
    los_candidatos=leer_candidaturas()
    los_votos=votos_para_candidato(los_candidatos)
    votos_en_total=total_de_votos(los_votos)
    mostar_porcentajes_de_votos(los_candidatos, los_votos, votos_en_total)

main()