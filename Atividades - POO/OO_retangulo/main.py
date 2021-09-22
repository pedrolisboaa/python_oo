"""
Fazer um programa para ler os valores da largura e altura
de um retângulo. Em seguida, mostrar na tela o valor de
sua área, perímetro e diagonal. Usar uma classe como
mostrado no projeto ao lado.
"""
from rectangle import Rectangle

print('Enter rectangle width and height:')
width = float(input())
height = float(input())
r1 = Rectangle(width, height)

print(f'AREA = {r1.area()}')
print(f'PERIMETER = {r1.perimeter()}')
print(f'DIAGONAL = {r1.diagonal()}')