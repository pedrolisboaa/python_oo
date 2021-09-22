"""
Dataclasses
"""
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('Pedro', 'Lisboa', 28)
# print(p1)
# print(p1.nome)
# print(p1.sobrenome)
# print(p1.nome_completo())