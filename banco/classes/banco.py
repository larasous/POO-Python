class Banco:
    def __init__(self):
        self.contas = []
        self.agencias = []
        self.clientes = []
      
    def add_conta(self, conta):
        self.contas.append(conta)    
        
    def add_cliente(self, cliente):
        self.clientes.append(cliente)   
    
    def add_agencia(self, agencia):
        self.agencias.append(agencia)
    
    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False

        if cliente.conta not in self.contas:
            return False

        if cliente.conta.agencia not in self.agencias:
            return False

        return True