class Account:
    def __init__(self, number):
        self.number = number
        self.total = 0

    def deposit(self, value):
        self.total += value

    def withdraw(self, value):
        self.total -= value

    def getTotal(self):
        return self.total


conta_helder = Account(123)

conta_helder.deposit(100)
print(conta_helder.total)

conta_helder.withdraw(20)
print(conta_helder.total)
