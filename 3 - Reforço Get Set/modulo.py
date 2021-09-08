# SETTER = Configurando um valor (=) - Setter configura - Somente se existir um getter
# GETTER = Obter um valor (.) - Getter lê - Pode existir sozinho

class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


p1 = Pessoa('marcelo')
print(p1.nome)