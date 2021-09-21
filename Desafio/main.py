from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Pedro', 28)
cliente2 = Cliente('Maria', 18)
cliente3 = Cliente('Juliana', 25)

conta1 = ContaPoupanca(1111, 235687, 0)
conta2 = ContaCorrente(2222, 321687, 0)
conta3 = ContaPoupanca(1112, 2187, 0)

cliente1.inserir_contar(conta1)
cliente2.inserir_contar(conta2)
cliente3.inserir_contar(conta3)

banco.inserir_conta(conta1)
banco.inserir_cliente(cliente1)


if banco.autenticar(cliente1):
    cliente1.conta.depositar(200)
    cliente1.conta.sacar(30)
else:
    print('Cliente não autenticado')