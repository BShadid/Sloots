def bonus_round():
    global money
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
    re = str(rere)
    print "In total, you earned $ %s from the bonus round." % re
    return rere
