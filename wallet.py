class wallet(object):
    def __init__(self, money):
        self.money = money
        
    def isEnoughMoney(self, price):
        if (self.money >= price):
            return True
        else:
            return False
        
    def winBet(self, bettedMoney):
        self.money += bettedMoney

    def loseBet(self, bettedMoney):
        self.money -= bettedMoney

    def print_balance(self):
        print "You have $", self.money, "remaining"

    def return_balance(self):
        return self.money
"""
swagMoney = wallet(1000)
print swagMoney.money
swagMoney.winBet(50)
print swagMoney.money

print swagMoney.isEnoughMoney(2000)
print swagMoney.isEnoughMoney(1000)
swagMoney.print_balance()
"""
