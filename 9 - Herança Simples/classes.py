class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'Oi meu nome é {self.nome}')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome} está comprando.')


class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
      # Pessoa.__init__(self, nome, idade) -> caso eu tivesse que pegar de outra ou pode ser assim mesmo
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'Eu {self.nome} {self.sobrenome} estou falando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome} está estudando.')

