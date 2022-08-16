class Pessoa:
    def __init__(self,nome,idade):
        self.nome= nome
        self.idade= idade
        self.nomeclasee=self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasee} Falando...')

class Cliente(Pessoa):
     def comprar(self):
        print(f'{self.nomeclasee} comprando...')

class Aluno (Pessoa):
    def estudar(self):
        print(f'{self.nomeclasee} estudando...')

class ClienteVIP(Cliente):
    pass