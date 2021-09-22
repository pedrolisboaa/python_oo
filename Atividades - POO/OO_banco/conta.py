class Conta:
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= (valor + 5)

    def mostrar_dados(self):
        return f'Account {self.numero}, Holder: {self.nome}, Balance: $ {self.saldo}'
