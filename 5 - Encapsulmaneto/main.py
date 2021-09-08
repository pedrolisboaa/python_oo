"""
Como é em outra linguagens
public, protect, private
_ privado mais fraco ou protect
__ privado mais forte
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


##################################################

bd = BaseDeDados()
bd.inserir_cliente(1, 'Pedro')
bd.inserir_cliente(2, 'Pedro Henrique')
bd.inserir_cliente(3, 'Pedro Henrique do Nascimento')
bd.inserir_cliente(4, 'Pedro Henrique do Nascimento Lisboa')
bd.lista_clientes()

bd.__dados = 'Maria'
bd.lista_clientes()