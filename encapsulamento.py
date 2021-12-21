"""
Modificadores de acesso em outras linguagens:
- public -> métodos e atributos que podem ser acessados dentro e fora da classe
- protected -> podem ser acessados apenas dentro da classe, ou filhas da mesma
- private -> atributos e/ou métodos está disponível apenas dentro da classe

Python possui convenções:
_ -> protected/private (public pois ainda permite acessar fora da classe)
__ -> pode acessar: (_NOMEDACLASSE__nomedoatributo), pode acessar e modificar

"""
class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property  # Faz com que o método pareça um atributo da classe
    def dados(self):
        return self.__dados
    
    
    def addClient(self, id, name):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: name}
        else:
            self.__dados['clientes'].update({id: name})
    
    def listClients(self):
        for id, name in self.__dados['clientes'].items():
            print(f'{id} - {name}')
    
    def removeClient(self, id):
        del self.__dados['clientes'][id]
        
        
bd = BaseDeDados()

bd.addClient(1, 'Luiz')
bd.addClient(2, 'Maria')
bd.addClient(3, 'João')
bd.addClient(4, 'Julia')

""" bd.__dados = 'Uma outra coisa' # Cria uma variavel sem gerar erros nos métodos da classe
print(bd.__dados)
print(bd._BaseDeDados__dados)  # Acessa o atributo da classe
 """
bd.removeClient(2)
print(bd.dados)  # por conta do construtor dados permite acessar


