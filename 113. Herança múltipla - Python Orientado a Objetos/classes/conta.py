from abc import ABC,abstractmethod



class Conta:
    def __init__(self,agencia,conta,saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo


    @saldo.setter
    def saldo(self,valor):
        if not isinstance(valor,(int,float)):
            raise ValueError('Valor do saldo nao e numerico')
        self._saldo =valor

    def depositar(self,valor):
        print(f'valor depositado = {valor} ')
        if not isinstance(valor,(int,float)):
            raise ValueError('Valor do deposito e numerico')
        self._saldo +=valor

    def detalhes(self):
        print(f'Agência: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}', end=' ')

    @abstractmethod
    def sacar(self,valor):
        pass