"""
1. Classe Bola: Crie uma classe que modele uma bola:
    a. Atributos: Cor, circunferência, material
    b. Métodos: trocaCor e mostraCor
"""

from bola import Bola

b1 = Bola('azul', 10, 'couro')
b1.mostrarCor()

b1.trocarCor('vermelho')
b1.mostrarCor()

print(b1.material)
print(b1.circunferencia)