from conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            self.detalhes()
            return

        self._saldo -= valor
        self.detalhes()