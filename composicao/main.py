"""
Composição
- Uma classe é dona de objetos de outra classe
"""
from classes import Cliente

c1 = Cliente('Luiz', 20)
c1.add_enderecos('Belo Horizonte', 'MG')
print(c1.name)
c1.list_enderecos()
del c1
print()

c2 = Cliente('Ana', 35)
c2.add_enderecos('Salvador', 'BA')
c2.add_enderecos('São Paulo', 'SP')
print(c2.name)
c2.list_enderecos()
del c2
print()

c3 = Cliente('Sofia', 27)
c3.add_enderecos('Rio de Janeiro', 'RJ')
print(c3.name)
c3.list_enderecos()
print()

print('#######################################')