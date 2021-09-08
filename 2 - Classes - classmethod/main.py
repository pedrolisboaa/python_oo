from pessoa import Pessoa

p1 = Pessoa('Pedro', 28)
p1.get_ano_nascimento()
print(p1.idade)
p1.get_ano_nascimento()

p2 = Pessoa.por_ano_nascimento('Juliana', 1996)
print(p2.nome, p2.idade)

print(p1.gerar_id())
print(Pessoa.gerar_id())