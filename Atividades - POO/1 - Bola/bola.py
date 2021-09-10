class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocarCor(self, cor):
        self.cor = cor 
    
    def mostrarCor(self):
        print(f'Minha cor é {self.cor}')
        