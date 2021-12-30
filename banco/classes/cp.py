from classes.conta import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('O valor precisa ser numérico')
    
        if self.saldo < valor:
            print('Saldo indisponível')
            return
        
        self.saldo -= valor
        self.detalhes()
            