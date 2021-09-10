class ContaCorrente:
    def __init__(self, numero, nomeTitular, saldo=0):
        self.numero = numero
        self.nomeTitular = nomeTitular
        self.saldo = saldo
    
    def alterarNome(self, novoNome):
        self.nome = novoNome
    
    def mostrarSaldo(self):
        saldoBonito = str(self.saldo)
        print(f"Saldo R$ {saldoBonito.replace(',','.')}")
    
    def depositar(self, valorDeDeposito):
        self.saldo += valorDeDeposito
    
    def saque(self, valorDeSaque):
        if not valorDeSaque > self.saldo:
            self.saldo -= valorDeSaque
            print(f'Saque realizado com sucesso.')
        else:
            print(f'Valor de saque excede seu saldo.')
    
    



    