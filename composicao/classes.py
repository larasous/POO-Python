class Cliente:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.enderecos = []
        
    
    def add_enderecos(self, cidade, estado):
        self.enderecos.append(Enderecos(cidade, estado))
        
    
    def list_enderecos(self):
        for endereco in self.enderecos:
            print(f"{endereco.cidade} - {endereco.estado}")

    
    def __del__(self):
        print(f'{self.name} FOI APAGADO')
    

class Enderecos:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
    
    
    def __del__(self):
        print(f'{self.cidade} - {self.estado} FOI APAGADO')