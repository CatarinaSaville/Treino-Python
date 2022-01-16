from conta import Conta
    
class ContaCorrente(Conta):
    def __init__(self, taxa, saldo, proprietario):
        super().__init__(saldo, proprietario)
        self.taxa = taxa

    def getTaxa(self):
        return self.taxa

    def setTaxa(self, taxa):
        self.taxa = taxa

    def getProjecaoSaldo(self, tempo):
        return self.saldo - (tempo * self.taxa)
        