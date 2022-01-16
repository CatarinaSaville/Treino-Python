from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, rendimento, saldo, proprietario):
        super().__init__ (saldo, proprietario)
        self.rendimento = rendimento

    def getRendimento(self):
        return self.rendimento

    def setRendimento(self, rendimento):
        self.rendimento = rendimento

    def getProjecaoRendimento(self, nmrMeses):
        return self.saldo + (nmrMeses * self.rendimento * self.saldo)
    