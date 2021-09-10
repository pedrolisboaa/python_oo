"""
3. Classe Retangulo: Crie uma classe que modele um retangulo:
a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a
quantidade de pisos e de rodapés necessárias para o local.
"""

from retangulo import Retangulo

print('Calculadora de Piso!')
ladoA = float(input('Digite o tamanho do lado A: '))
ladoB = float(input('Digite o tamanho do lado B: '))

rec1 = Retangulo(ladoA, ladoB)
areaTotal = rec1.calcularArea()
perimetro = rec1.calcularPerimetro()

print(f'Sua área possui {areaTotal}.')
print(f'O périmetro é de {perimetro}')



