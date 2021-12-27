class Pessoa:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} Falando..')
    

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} Comprando..')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} Estudando..')