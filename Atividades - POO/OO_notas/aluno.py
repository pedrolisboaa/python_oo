class Aluno:
    def __init__(self, nome, nota_1, nota_2, nota_3):
        self.nome = nome
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.nota_3 = nota_3

    def nota_final(self):
        return self.nota_1 + self.nota_2 + self.nota_3

    def resposta_final(self):
        if Aluno.nota_final(self) >= 60:
            return f'PASS'

        return f'FAILED\nMISSING {60 - self.nota_final()} POINTS'
