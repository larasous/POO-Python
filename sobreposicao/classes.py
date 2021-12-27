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

    
    def falar(self):
        print(f'Estou em CLIENTE.')


class ClienteVIP(Cliente):
    def __init__(self, name, age, last_name):
        Pessoa.__init__(self, name, age)
        self.last_name = last_name
    
    
    # sobrescrevendo o método falar
    def falar(self):
        Pessoa.falar(self)
        super().falar()  # chamando o método falar da super classe (busca a primeira classe que possui o método falar)
        print(f'{self.name} {self.last_name} está falando')