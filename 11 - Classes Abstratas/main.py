from contaPoupanca import ContaPoupanca
from contaCorrente import ContaCorrente

cp = ContaPoupanca(15, 111, 500)
print(cp.saldo)
cp.sacar(100)
print(cp.saldo)
cp.sacar(500)

print("+==================")

cc = ContaCorrente(1111, 333, 0)
cc.sacar(50)