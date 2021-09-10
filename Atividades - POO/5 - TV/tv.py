class Televisao:
    def __init__(self, canal=0, volume=0):
        self.canal = canal
        self.volume = volume
    
    def subirCanal(self):
        if self.canal < 20:
            self.canal += 1
            print(f'Canal {self.canal}')
        else:
            print(f'Canal {self.canal}')
    
    def descerCanal(self):
        if self.canal > 1:
            self.canal -= 1
            print(f'Canal {self.canal}')
        else:
            print(f'Canal {self.canal}')
    
    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 10
            print(f'Volume {self.volume}')
        else:
            print(f'Volume {self.volume}')
    
    def diminuirVolume(self):
        if self.volume > 1:
            self.volume -= 10
            print(f'Volume {self.volume}')
        else:
            print(f'Volume {self.volume}')