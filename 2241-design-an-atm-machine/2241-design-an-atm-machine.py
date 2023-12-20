class ATM:
    def __init__(self):
        self.cash = [0] * 5
        self.values = [20, 50, 100, 200, 500]
    def deposit(self, banknotesCount):
        for ind, val in enumerate(banknotesCount):
            self.cash[ind] += val
    def withdraw(self, amount):
        res = []
        for cash, val in zip(self.cash[::-1], self.values[::-1]):
            amt = min(cash, amount // val)
            res = [amt] + res
            amount -= (amt * val)
        if amount == 0:
            self.deposit([-x for x in res])
            return res
        else:
            return [-1]
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)