from classes.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None
        
    def add_conta(self, conta):
        self.conta = conta