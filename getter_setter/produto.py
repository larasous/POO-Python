"""
Getter - obtém um valor
Setter - configura um valor

Primeiro, vai para o getter, em seguida, para o setter, configurando o valor
"""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        self._nome = value.title()
    
    # Getter 
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, value):
        if isinstance(value, str):
            value = float(value.replace('R$',''))
        self._preco = value

p1 = Produto("CAMISETA", 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto("CANECA", 'R$15')
p2.desconto(10)
print(p2.nome,p2.preco)