#Hi Griff
#Version 0.6.1

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
    print "Three Bonus:     BONUS GAME"
    print " "

def bonus_round():
    a = random.randint(0,5)
    b = random.randint(5,10)
    c = random.randint(-30,20)
    print "Welcome to the bonus round! In this mode, three random numbers will"
    print "be added together, then your bet will be returned times the sum of "
    print "these numbers. Good luck and may RNGesus be with you."
    print " "
    print "This doesn't work right now..."

def bonus_round2(n):
    global score
    roundy = 0
    print "Welcome to the bonus round! In this game mode,"
    print "you will be offered an initial money value"
    print "that is given to you as a bonus. You can change"
    print "the bonus offer amount up to 3 times, but it"
    print "has an equal chance of increasing as decreasing!"
    print "After 3 changes, you are required to take the"
    print "fourth and final offer. Good luck!"
    print " "
    print " "
    init_off = random.randint(1, 200)
    print "OFFER:" + str(init_off)
    print " "
    while roundy < 3:
        x = raw_input("Would you like to change the offer? (Y/N)").lower()
        if x == "y":
            init_off += random.randit(-300,300)
            roundy += 1
            print init_off
        elif x == "n":
            roundy = 3
        else:
            print "Please input either 'y' or 'n'"
    rere = init_off + money
    score += rere
    re = str(rere)
    print "In total, you earned $ %s from the bonus round." % re

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

        
    options = ["7", "Churry", "Churry", "Churry", "Churry", "Churry","Blanabber","Bonus", "Bonus", "Bonus", "Blanabber","Blanabber","Blanabber","Gurps","Gurps", "Gurps", "BAR", "BAR", "Mystery"]
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
            one = options[random.randint(0,18)]
            two = options[random.randint(0,18)]
            three = options[random.randint(0,18)]
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
                elif one == "Bonus":
                    bonus_round2(money)
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
