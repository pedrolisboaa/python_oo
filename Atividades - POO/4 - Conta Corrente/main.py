"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, 
com valor default zero e os demais atributos são obrigatórios.
"""
from conta import ContaCorrente

conta = ContaCorrente(123, 'Pedro')
conta.depositar(1000)
conta.mostrarSaldo()
conta.depositar(100.50)
conta.mostrarSaldo()
conta.saque(500.38)
conta.mostrarSaldo()
conta.saque(601)
conta.mostrarSaldo()