"""
2. Classe Quadrado: Crie uma classe que modele um quadrado:
    a. Atributos: Tamanho do lado
    b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""

from quadrado import Quadrado

q1 = Quadrado(10)

q1.mostrarValorDoLado()
q1.calcularArea()

print('==============')
q1.mudarValorDoLado(20)
q1.mostrarValorDoLado()
q1.calcularArea()