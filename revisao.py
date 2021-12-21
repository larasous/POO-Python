# Setter -> Configurar um valor(=)
# Getter -> Obter um valor (.)
# Não existe setter sem getter
# Getter e Setter possuem o mesmo nome
class Pessoa:
    def __init__(self, nome):
        self._nome = nome # torna o atributo "privado" por conta do underline

    @property  # GETTER
    def nome(self):
        return self._nome

    @nome.setter  # SETTER
    def nome(self, nome):
        self._nome = nome

    @property
    def sobrenome(self):
        return 'Desconhecido'


p1 = Pessoa('Otávio')
print(p1.nome)
print(p1.sobrenome)