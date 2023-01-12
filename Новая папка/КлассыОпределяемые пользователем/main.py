class Worker:
    def _init_(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split() [-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
        bob = Worker('Bob Smithc', 50000)
        sue = Worker()
        bob.lastName()
        sue.lastName()
        sue.giveRaise(.10)
        sue.pay