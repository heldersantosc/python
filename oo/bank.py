class Account(object):
    def __init__(self, number):
        self.number = number
        self.__total = 0

    def deposit(self, value):
        self.__total += value

    def withdraw(self, value):
        self.__total -= value

    def getTotal(self):
        return self.__total


class Bank(Account):
    def __init__(self, number, cvv):
        super(Bank, self).__init__(number)
        self.cvv = cvv

    def withdraw(self, value):
        self._Account__total -= value


conta_helder = Bank(123, 223)

conta_helder.deposit(100)
print(conta_helder.getTotal())

conta_helder.withdraw(20)
print(conta_helder.getTotal())

print(conta_helder.cvv)
