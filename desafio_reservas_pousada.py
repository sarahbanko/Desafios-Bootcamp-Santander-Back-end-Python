def reservas(quartos_disponiveis, reservas_solicitadas):
    confirmadas = []
    recusadas = []

    for quarto in reservas_solicitadas:
        if quarto in quartos_disponiveis:
            confirmadas.append(quarto)
            quartos_disponiveis.remove(quarto)
        else:
            recusadas.append(quarto)
            
    print("Reservas confirmadas:", " ".join(str(q) for q in confirmadas))
    print("Reservas recusadas:", " ".join(str(q) for q in recusadas))

def main():
    entrada_1 = input()
    entrada_2 = input()

    quartos_disponiveis = list(map(int, entrada_1.strip().split()))
    reservas_solicitadas = list(map(int, entrada_2.strip().split()))

    reservas(quartos_disponiveis, reservas_solicitadas)

main()