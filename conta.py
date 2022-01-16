class Conta:
    def __init__(self, saldo, proprietario):
        self.saldo = saldo
        self.proprietario = proprietario

    def getSaldo(self):
        return self.saldo

    def getProprietario(self):
        return self.proprietario

    def setSaldo(self, saldo):
        self.saldo =saldo

    def setProprietario(self, proprietario):
        self.proprietario = proprietario

    def depositar(self, depositar):
        self.saldo = self.saldo + depositar

    def sacar(self, sacar):
        self.saldo = self.saldo - sacar