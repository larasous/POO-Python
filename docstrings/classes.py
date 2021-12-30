"""Descrição rápida e simples

Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Vivamus dolor neque, euismod sed porta quis, scelerisque at libero. 
Phasellus massa nibh, accumsan id enim vel, egestas finibus dui. 
Sed euismod, dolor vitae consectetur blandit, diam orci lobortis ex, non laoreet elit nulla eu erat. 
Sed cursus arcu id ipsum rhoncus hendrerit. Cras dapibus lobortis justo, at dignissim tortor. 
Vestibulum pharetra ex in commodo posuere. Nam elementum enim sed tortor ornare placerat. 
Pellentesque rhoncus congue sapien ac posuere.
"""

class A:
    """Documentação normal
    
    Conforme qualquer outra documentação
    """
    atr1 = 1
    atr2 = 2
    
    def __init__(self, msg):
        """Inicializa os dados

        Args:
            msg (string): mensagem ou texto da classe
        """
        self.msg = msg

    @staticmethod
    def exibe_msg(msg):
        """Método que exibe um texto de até 100 caracteres na tela

        Args:
            msg (str): texto de até 100 caracteres
            
        Return:
            msg (str): texto de até 100 caracteres]
            
        Raises:
            ValueError: se o texto tiver mais de 100 caracteres
            TypeError: se o texto não for do tipo str
        """
        if not isinstance(msg, str):
            raise TypeError('O texto precisa ser uma string')
        
        if len(msg) > 100:
            raise ValueError('O texto precisa ter 100 caracteres ou menos')

        return msg