from escritor import Escritor
from caneta import Caneta
from maquina import MaquinaDeEscrever

escritor1 = Escritor('Mariazinha')
caneta1 = Caneta('Bic')
maquina1 = MaquinaDeEscrever()

escritor1.ferramenta = caneta1
escritor1.ferramenta.escrever()

escritor1.ferramenta = maquina1
escritor1.ferramenta.escrever()