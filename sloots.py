#Hi Griff
#Version 0.4.2

import random
import time


def wait(n):
    time.sleep(n)

round = 1
score = 100
        
def instructions():
    print "I   N   S   T   R   U   C   T   I   O   N   S"
    print "You can spin the slots as long as you have"
    print "money. The lowest buy in is $5. The amount of"
    print "money you receive for winning is based on the"
    print "amount of money you bet. The higher your risk"
    print "the higher your reward. The rewards are:"
    print " "
    print "Three Churries:  2 x bet      Two Churries:  1 x bet"
    print "Three Blannervy: 5 x bet      Two Blannervy: 2.5 x bet"
    print "Three Gurps:     7 x bet      Two Gurps:     3.5 x bet"
    print "Three BAR:       10 x bet     Two BAR:       5 x bet"  
    print "Three 7s:        25 x bet     Two 7s:        12.5 x bet"
    print "Three Mystery:   BONUS ROUND"
    print " "

def bonus_round():
    a = random.randint(0,5)
    b = random.randint(5,10)
    c = random.randint(-30,20)
    print "Welcome to the bonus round! In this mode, three random numbers will"
    print "be added together, then your bet will be returned times the sum of "
    print "these numbers. Good luck and may RNGesus be with you."
    

def sloots():
    global score
    global round
    print " "
    print "Money: $ %s" % score
    print " "
    t = True
    while (t):
        money = raw_input("How much money would you like to bet? $")
        try:
            money = float(money)
            if money < 5.0:
                print "Put in more money."
            elif money > 5000:
                print "Sorry, that is too much money. Please enter a lower amount."
            elif money > score:
                print "Insufficient funds. Please try again."
            else:
                score -= money
                t = False
        except:
            print "That doesn't work"

        
    options = ["7", "Churry", "Churry", "Churry", "Churry", "Churry","Blanabber","Blanabber","Blanabber","Blanabber","Gurps","Gurps", "Gurps", "BAR", "BAR", "Mystery"]
    yes = True
    while (yes):
        a = raw_input("Are you ready to spin? (Y/N) ").lower()
        if a != "y" and a !="n":
            print "Please enter either 'y' or 'n'"
        elif a == "n":
            print "Then why did you select this game in the first place?"
            yes = False
            
        elif a == "y":
            print " "
            print "Spinning..."
            wait(1)
            print "."
            wait(1)
            print "."
            wait(1)
            print "."
            wait(2)
            print " "
            yes = False
    if a == "y":
        true = True
        while (true):
            one = options[random.randint(0,15)]
            two = options[random.randint(0,15)]
            three = options[random.randint(0,15)]
            print " "
            print one
            wait(1)
            print two
            wait(1)
            print three
            wait(1)
            print " "
            if one == two and two == three:
                wait(1)
                print "Three of a kind!"
                if one == "Churry":
                    score += money * 3
                elif two == "Blanabber":
                    score += money * 6
                elif three == "Gurps":
                    score += money * 8
                elif one == "BAR":
                    score += money * 11
                elif one == "Mystery":
                    print "This will come later... Returning money"
                    score += money
                elif one == "7":
                    score += money * 26
            elif one == two or one == three:
                wait(1)
                print "Two of a kind!"
                if one == "Churry":
                    score += money * 2
                elif one == "Blanabber":
                    score += money * 3.5
                elif one == "Gurps":
                    score += money * 4.5
                elif one == "BAR":
                    score += money * 6
                elif one == "7":
                    score += money * 13.5
            elif two == one or two == three:
                wait(1)
                print "Two of a kind!"
                if two == "Churry":
                    score += money * 2
                elif two == "Blanabber":
                    score += money * 3.5
                elif two == "Gurps":
                    score += money * 4.5
                elif two == "BAR":
                    score += money * 6
                elif two == "7":
                    score += money * 13.5
            
            else:
                print "Sorry! Better luck next time!"
            true = False

    
    print " "
    print "Total money: %s" % score
    print " "
    
    wait(2)

    round += 1

def init():
    global score
    x = True
    while (x):
        rounds = raw_input("Would you like to play? (Y/N)").lower()
        if rounds == "y":
            if score > 5:
                sloots()
            else:
                print "YOU DO NOT HAVE ENOUGH MONEY TO PLAY. GAME OVER"
                x = False
        elif rounds == "n":
            print " "
            x = False
        else:
            print "Please input either 'y' or 'n'"

    print "Return: %s" %score

instructions()
init()

awoiefhawe = raw_input("Press enter to close")
