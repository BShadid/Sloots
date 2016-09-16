from Cards import *
def g_deck(suits,cards):
    lst = []
    for s in suits:
        for c in cards:
            lst.append((c,s))
    return lst

suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
cards = ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",\
         "Queen", "King"]

deck = Cards(g_deck(suits,cards))
deck.shuffle()
dealer = []
player = []

def beginning(deck,dealer,player):
    for x in range(0,2):
        dealer.append(deck.deck[0])
        deck.draw()
    for x in range(0,2):
        player.append(deck.deck[0])
        deck.draw()
    return deck,dealer,player

beginning(deck,dealer,player)

def val(hand):
    val = 0
    for c in hand:
        if c[0] == "Jack" or c[0] == "Queen" or c[0] == "King":
            val += 10
        elif c[0] == "Ace":
            if val + 11 > 21:
                val += 1
            if val + 11 <= 21:
                val += 11
        else:
            val += int(c[0])
    return val


def hit(hand,deck):
    hand.append(deck.deck[0])
    deck.draw()
    return deck,hand

def winner(player,dealer):
    if player > dealer and player < 22:
        return "Player wins!"
    if dealer > player and dealer < 22:
        return "Dealer wins!"
    if dealer == player:
        return "Push!"
    else:
        return "Somebody busted..."

if __name__ == "__main__":    
    stand_d = False
    stand_p = False
    both_stand = False
    p_bust = False
    d_bust = False
    while both_stand != True:
        print "Dealer" ,val(dealer)
        
        if val(dealer)>21:
            print "Dealer bust"
            both_stand = True
            d_bust = True
        
        if val(player)>21:
            print "Player bust"
            both_stand = True
            p_bust = True
            
        if val(dealer) < 14:
            hit(dealer,deck)
            
        if val(dealer) > 14:
            stand_d = True
            
        print "Player:", val(player)
        
        if stand_p == False:
            c = raw_input("Hit or stand? ").lower()
            if c == "h" or c == "hit":
                hit(player,deck)
            if c == "s" or c == "stand":
                stand_p = True
        
        if stand_p and stand_d:
            both_stand = True
    
    print "Dealer:" , val(dealer)
    print "Player:" , val(player)
    
    if p_bust:
        print "The player busted."
    if d_bust:
        print "The dealer busted."
    else:
        print winner(val(player),val(dealer))
 

        

            
