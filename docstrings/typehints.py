"""Documentação deste módulo

Não faz nada, é apenas um exemplo.
Typing - https://docs.python.org/3/library/typing.html
"""
from typing import Union

x: int = 10
y: float = 2.3
z: bool = True

def funcao(p1: int, p2: float, p3: str) -> tuple:
    return p1, p2, p3

print(funcao(12, 34.5, 'ola'))

def funcao2(p1: int, p2: float, p3: int) -> Union[int, float]:
    pass