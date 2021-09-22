"""
Fazer um programa para ler os dados de um produto em estoque (nome, preço e
quantidade no estoque). Em seguida:
• Mostrar os dados do produto (nome, preço, quantidade no estoque, valor total no
estoque)
• Realizar uma entrada no estoque e mostrar novamente os dados do produto
• Realizar uma saída no estoque e mostrar novamente os dados do produto
"""
from produto import Produto

print('Enter product data:')
name = input('Name: ')
price = float(input('Price: '))
quantity = int(input('Quantity in stock: '))
product = Produto(name, price, quantity)


print(f'Product data: {product.atualizar()}')
value = int(input('Enter the number of products to be added in stock: '))
product.adicionar_produto(value)

print(f'Updated data:: {product.atualizar()}')
value = int(input('Enter the number of products to be removed from stock: '))
product.remover_produto(value)

print(f'Updated data:: {product.atualizar()}')

