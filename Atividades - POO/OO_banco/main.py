"""
Em um banco, para se cadastrar uma conta bancária, é necessário informar o número da conta, o nome do
titular da conta, e o valor de depósito inicial que o titular depositou ao abrir a conta. Este valor de depósito
inicial, entretanto, é opcional, ou seja: se o titular não tiver dinheiro a depositar no momento de abrir sua
conta, o depósito inicial não será feito e o saldo inicial da conta será, naturalmente, zero.
Importante: uma vez que uma conta bancária foi aberta, o número da conta nunca poderá ser alterado. Já
o nome do titular pode ser alterado (pois uma pessoa pode mudar de nome por ocasião de casamento, por
exemplo).
Por fim, o saldo da conta não pode ser alterado livremente. É preciso haver um mecanismo para proteger
isso. O saldo só aumenta por meio de depósitos, e só diminui por meio de saques. Para cada saque
realizado, o banco cobra uma taxa de $ 5.00. Nota: a conta pode ficar com saldo negativo se o saldo não for
suficiente para realizar o saque e/ou pagar a taxa.
Você deve fazer um programa que realize o cadastro de uma conta, dando opção para que seja ou não
informado o valor de depósito inicial. Em seguida, realizar um depósito e depois um saque, sempre
mostrando os dados da conta após cada operação
"""

from conta import Conta
numero = int(input('Enter account number: '))
nome = input('Enter account holder: ')
resposta = input('Is there na initial deposit (y/n)? ')

if resposta == 'y':
    saldo = float(input('Enter initial deposit value: '))
    conta = Conta(numero, nome, saldo)
else:
    conta = Conta(numero, nome)

print(f'Account data:')
print(conta.mostrar_dados())

valor = int(input('Enter a deposit value: '))
conta.deposito(valor)
print('Updated account data:')
print(conta.mostrar_dados())

valor = int(input('Enter a withdraw value: '))
conta.sacar(valor)
print('Updated account data:')
print(conta.mostrar_dados())