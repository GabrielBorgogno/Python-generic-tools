from conta_poupanca import ContaPopanca
from conta_corrente import  ContaCorrente

cp= ContaPopanca(1111,2222,0)
print('\n')
cp.depositar(1000)
print('\n')
cp.depositar(300)
print('\n')
cp.depositar(500)
print('\n')
cp.sacar(1000)
print('\n')
cc = ContaCorrente(1111,2222,0,500)
print('\n')
cc.depositar(5000)
cc.sacar(600)