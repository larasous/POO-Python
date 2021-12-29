"""
Gerenciadores de contexto - Criando e usando
"""

# 1ª Forma de criar o gerenciador
class Arquivo:
    def __init__(self, arquivo, modo):
        print('Abrindo arquivo')
        self.arquivo = open(arquivo, modo)
       
    def __enter__(self):
        print('Retornando arquivo')
        return self.arquivo
    
    def __exit__(self, exc_type, exc_value, trace):
        print('Fechando arquivo')
        self.arquivo.close()
        # Tratando a exceção
        return True
    
with Arquivo('abc.txt', 'w+') as file:
    file.write('Alguma coisa') 


# 2ª forma de criar um gerenciador
from contextlib import contextmanager

@contextmanager
def abrir(arq, modo):
    try:
        print('Abrindo arquivo')
        arq = open(arq, modo)
        yield arq
    finally:
        print('Fechando arquivo')
        arq.close()
        

with abrir('abc.txt', 'w') as file:
    file.write('Alguma outra coisa\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n') 