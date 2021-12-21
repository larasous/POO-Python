class A:
    vc = 123
    
    """ def __init__(self):  # altera em cada instância criada
        self.vc = 100 """
    
a1 = A()
a2 = A()

a1.vc = 321 # altera somente na instância a1
print(a1.vc)
print(a2.vc)
print(A.vc)

print('\n')

A.vc = 'Alterado' # altera na classe, e instâncias que possuem o mesmo valor da classe
print(a1.vc)
print(a2.vc)
print(A.vc)

"""
print('\n')
# com o def init:
print(A.vc) # permanece o valor pois não é uma instância
print(a1.vc) # recebe o valor que está na função
print(a2.vc) """