class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    
    def mudarValores(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    
    def retornarValoresDosLados(self):
        return f'lado a: {self.ladoA} \nlado b: {self.ladoB}'
    
    def calcularArea(self):
        area = self.ladoA * self.ladoB
        return area
    
    def calcularPerimetro(self):
        perimetro = (self.ladoA * 2) + (self.ladoB * 2)
        return perimetro
