
def cadastro_paciente(n):
    pacientes = []
    for _ in range(n):
        linha = input().strip()
        nome, idade, status = linha.split(", ")
        nome = nome.strip()
        idade = int(idade.strip())
        status = status.strip()
        pacientes.append((nome, idade, status))
    return pacientes 

def ordem_prioridade(pacientes):
    fila = []
    for index, (nome, idade, status) in enumerate(pacientes):
        if "urgente" in status:
            prioridade = 0
            desempate = -idade
        elif idade >= 60:
            prioridade = 1
            desempate = index
        else:
            prioridade = 2
            desempate = index
        fila.append((prioridade, desempate, index, nome))
    fila.sort()
    return [nome for _, _, _, nome in fila]

def main():
    n = int(input())
    pacientes = cadastro_paciente(n)
    ordem = ordem_prioridade(pacientes)
    print("Ordem de Atendimento: " + ", ".join(ordem))

main()