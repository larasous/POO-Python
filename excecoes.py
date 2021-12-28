"""
Criando exceções em Python
"""

class TaErradoError(Exception):
    pass


def teste():
    raise TaErradoError('Errado!!')

try:
    teste()
except TaErradoError as error:
    print(f'Erro: {error}')