from Eletronico import Eletronico
from  Log import LogMixin

class Smartphone(Eletronico,LogMixin):
    def __init__(self, nome):
        super().__init__(nome)

        self._conectado = False


    def conectar(self):
        if not self._ligado:
            error= f'{self.nome} nao esta ligado'
            self.log_error(error)
            return

        if self._conectado:
            error = f'{self.nome} já esta conectado'
            self.log_error(error)
        self._conectado = True


    def desconectar(self):

         if self._conectado:
           error=f'{self.nome} não  esta conectado'
           self.log_error(error)
           return

         info = f'{self.nome} foi desligado com sucesso'
         print(info)
         self.log_info(info)
         self._conectado = False