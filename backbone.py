#hi griff
#dummy game

import random
from wallet import wallet 
class game(object):

    def __init__(self, w):
        self.wallet = w

    def play_game(self):
        i = 0
        while i < 20:
            if self.wallet.isEnoughMoney(100):
                a = random.randint(0,1)
                if a == 1:
                    self.wallet.winBet(100)
                    print "You win!"
                    w1.print_balance()        
                else:
                    self.wallet.loseBet(100)
                    print "You lose."
                    w1.print_balance()        
            else:
                print "You don't have enough money."
                break
            i += 1

        return self.wallet
    
w1 = wallet(1000)
g = game(w1)
w1.print_balance()        
g.play_game()
