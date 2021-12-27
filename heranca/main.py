"""
Associação - Usa
Agregação - Tem
Composição - É dono
Herança - É
"""
from classes import *

c1 = Cliente('Luiz', 24)
print(c1.name)
c1.falar()
c1.comprar()

print()

a1 = Aluno('Sofia', 23)
print(a1.name)
a1.falar()
a1.estudar()