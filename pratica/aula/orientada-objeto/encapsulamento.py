class ContaBancaria:
    
    def __init__(self, titular, saldo_inicial = 0):
        self.titular = titular
        self.__saldo = saldo_inicial # atributo privado

    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido.")

conta_a = ContaBancaria(titular="Maria", saldo_inicial=200)
conta_b = ContaBancaria(titular="Alexandre", saldo_inicial=40000)

print(conta_a.titular)
print(conta_a.get_saldo())
# print(conta_a.__saldo_inicial)

conta_a.depositar(2000)
conta_a.depositar(100)
conta_a.sacar(2100)
print(conta_a.get_saldo())

print(conta_b.get_saldo())
conta_b.depositar(1_000_000)

print(conta_b.get_saldo())


