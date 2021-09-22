class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total_estoque(self):
        return self.preco * self.quantidade

    def adicionar_produto(self, valor):
        self.quantidade += valor

    def remover_produto(self, valor):
        self.quantidade -= valor

    def atualizar(self):
        return f'{self.nome}, $ {self.preco}, {self.quantidade}, units, Total: $ {self.valor_total_estoque()}'

