print("Conta bancaria")

from conta import Conta
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca


contas = ContaPoupanca(0.1, 10000, "catarina")
conta2 = ContaCorrente(10, 1000,"cau")



print("o que voce deseja fazer na sua conta?")
print("1-ver saldo")
print("2-depositar")
print("3-sacar")
print("4-ver projecao")
print("5-sair")

while True: 
    acao = input("digite o numero da acao\n")
        
    if acao == "1":
        print(contas.getSaldo())
    elif acao == "2":
        contas.depositar(int(input("qual valor vc deseja depositar?: ")))
    elif acao == "3":
        contas.sacar(int(input("qual valor vc deseja sacar?: ")))
    elif acao == "4":
        print(contas.getProjecaoRendimento(int(input("de que mes vc deseja ver o rendimento?: "))))
    elif acao == "5":
        break
