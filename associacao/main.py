"""
Associação
- Duas classes se associam uma a outra, porém, não dependem entre si
"""
from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Luna')
caneta = Caneta('Stabillo')
maquina = MaquinaDeEscrever()

""" Associação 
escritor.ferramenta = caneta  # atributo ferramenta recebe um objeto
escritor.ferramenta.escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever() """

del escritor # apaga o escritor, porém, as outras instâncias continuam existindo
print(caneta.marca)
maquina.escrever()