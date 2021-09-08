from carrinho_de_compras import CarrinhoDeCompras
from produto import Produtos

carrinho = CarrinhoDeCompras()
p1 = Produtos('Camiseta', 50)
p2 = Produtos('Iphone', 1150)
p3 = Produtos('Caneca', 20)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)


carrinho.lista_produtos()
print(carrinho.somar_total())

del carrinho
carrinho.lista_produtos()
