class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def mudarValorDoLado(self, novolado):
        self.lado = novolado
    
    def mostrarValorDoLado(self):
        print(f'eu tenho lado de {self.lado}')
    
    def calcularArea(self):
        area = self.lado ** 2
        print(f'Minha área é de {area}')