from contaPoupanca import ContaPoupanca

from contaCorrente import ContaCorrente

conta1 = ContaPoupanca(0.1, 10000, "catarina")

conta2 = ContaCorrente(10, 1000,"cau")

print (conta2.getProjecaoSaldo(5))

print (conta1.getSaldo())

conta1.depositar(100)

print (conta1.getSaldo())

conta1.sacar(150)

print (conta1.getSaldo())

print (conta1.getProjecaoRendimento(6))
