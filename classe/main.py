from pessoa import Pessoa

# instanciando a classe, criando objetos
p1 = Pessoa('Luiz', 29)
p2 = Pessoa('Maria', 18)

p1.falar('POO')
p2.falar('filmes')
p1.comer('Churrasco')
p2.comer('Carne')
p1.parar_falar()
p2.parar_falar()
p1.comer('Churrasco')
p2.comer('Carne')
print(p2.get_ano_nascimento())