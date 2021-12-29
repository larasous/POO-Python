"""
Em Python tudo é objeto, incluindo as classes
Metaclasses são as "classes" que criam outras classes.
"""
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        
        # tratando a exceção de chamar um método que não existe
        if 'b_fala' not in namespace:
            print(f'Você deve criar o método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala deve ser um método e não atributo em {name}')
        
        return type.__new__(mcs, name, bases, namespace)
    
class A(metaclass=Meta):
    def falar(self):
        self.b_fala()
    
class B(A):
    def b_fala(self):
        print('OI')