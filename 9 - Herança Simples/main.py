"""
Associação - USA | Agregação - TEM | Composição -  É DONO | Herança - É
"""

from classes import *

c1 = Cliente('Pedro', 28)
print(c1.nome)
c1.falar()
c1.comprar()

a1 = Aluno('Olívia', 1)
print(a1.nome)
a1.falar()
a1.estudar()

c2 = ClienteVip('Moises', 69, 'Silva')
c2.falar()