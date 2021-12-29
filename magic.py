"""
Métodos mágicos: https://rszalski.github.io/magicmethods/
São os métodos que possuem __ no início e fim. Ex.: __init__
"""
class A:
    #  primeiro método a ser chamado na instância de um objeto
    def __new__(cls, *args, **kwargs):
        print('Método new foi chamado')

        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = super().__new__(cls)

        return cls._jaexiste

    # permite que uma instância de uma classe seja chamada como uma função
    def __call__(self, *args, **kwargs):
        return f'Argumentos enviados: {args} {kwargs}'

    # retorna o comprimento
    def __len__(self):
        return 55

    # inicializador da classe
    def __init__(self, nome=None):
        print('INIT')

    # define o comportamento para quando str é chamado em uma instância
    def __str__(self):
        return f'O que quero exibir quando essa classe se transformar em uma str'

    # define o comportamento para quando um objeto é coletado como lixo
    def __del__(self):
        print('Objeto coletado.')

    # define o comportamento para atribuição a um atributo, mesmo ele existindo ou não
    def __setattr__(self, key, value):
        self.__dict__[key] = f'{value} adicionei isso no seu valor'


a = A('luiz otávio')