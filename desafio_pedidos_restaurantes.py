class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, quantidade_pedidos):
        for _ in range (quantidade_pedidos):
            nome, preco = input().rsplit(" ", 1)
            self.itens.append((nome.strip(), float(preco)))
           
    def calcular_total(self):
        return sum(preco for _, preco in self.itens)


quantidade_pedidos = int(input().strip())
pedido = Pedido()
pedido.adicionar_item(quantidade_pedidos)

print(f'{pedido.calcular_total():.2f}')