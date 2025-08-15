from datetime import datetime


class Veiculos:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def verificar_antiguidade(self):
        data_atual = datetime.now().year
        idade = data_atual - self.ano

        if idade > 20:
            return "Veículo antigo"
        else:
            return "Veículo novo"

marca = input().strip()
modelo = input().strip()
ano = int(input().strip())

# Instanciando o objeto e verificando a antiguidade
veiculo = Veiculos(marca, modelo, ano)
print(veiculo.verificar_antiguidade())