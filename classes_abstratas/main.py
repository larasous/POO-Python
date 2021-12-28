from classes.cp import ContaPoupanca
from classes.cc import ContaCorrente

cp1 = ContaPoupanca(1111, 2222, 0)
cp1.detalhes()
cp1.depositar(25)
cp1.sacar(34)

print("#########################################")
      
cc1 = ContaCorrente(2222, 4444, 0, 500)
cc1.depositar(100)
cc1.sacar(250)
cc1.sacar(500)
cc1.depositar(1000)
