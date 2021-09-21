"""
class Arquivo:
    def __init__(self, arquivo, modo):
        print('init')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Entrou na classe')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Saiu da classe')
        self.arquivo.close()


with Arquivo ('abc.txt', 'w') as arquivo:
    arquivo.write('Oi gente!')

"""

from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        arquivo.close()


with abrir('bcd.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')