from classes import Cliente

cliente1 = Cliente('Pedro', 28)
cliente1.insere_endereco('Brasília', 'DF')
cliente1.insere_endereco('Goiania', 'GO')

cliente2 = Cliente('Rosangela', 64)
cliente2.insere_endereco('Jardim Botânico', 'DF')
cliente2.insere_endereco('Copacabana', 'RJ')


cliente1.lista_endereco()
cliente2.lista_endereco()