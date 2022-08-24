from conta import   Conta

class ContaPopanca(Conta):
    def sacar(self,valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()
