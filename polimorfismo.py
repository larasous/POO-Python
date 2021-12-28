"""
Polimorfismo é o princípio que permite que classes derivadas de uma mesma
superclasse tenham métodos iguais (mesma assinatura), mas comportamentos diferentes

Mesma assinatura = Mesma quantidade e tipos de parâmetros
"""
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def falar(self):
        pass
    

class B(A):
    def falar(self, msg):
        print(f'B está falando {msg}')
        

class C(A):
    def falar(self, msg):
        print(f'C está falando {msg}')

b = B()
c = C()

b.falar('UM ASSUNTO')
c.falar('OUTRO ASSUNTO')