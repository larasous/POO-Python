from log import LogMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False
    
    def ligar(self):
        if self._ligado:
            return
        print(f'{self._nome} está ligado')
        self._ligado = True
    
    def desligar(self):
        if not self._ligado:
            return
        print(f'{self._nome} está desligado')
        self._ligado = False
        

class Smartphone(Eletronico, LogMixin):  # herança múltipla
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False
        
    def conectar(self):
        if not self._ligado:
            error = f'{self._nome} não está ligado'
            print(error)
            self.log_error(error)
            return
        
        if self._conectado:
            error = f'{self._nome} já está conectado'
            print(error)
            self.log_error(error)
            return
        
        info = f'{self._nome} está conectado'
        print(info)
        self.log_info(info)
        self._conectado = True
            
    
    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} não está conectado'
            print(error)
            self.log_error(error)
            return
        
        info = f'{self._nome} foi desconectado'
        print(info)
        self.log_info(info)
        self._conectado = False