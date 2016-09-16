import random
class Cards(object):

   def __init__(self,deck):
      self.deck = deck
   
   def shuffle(self):
      random.shuffle(self.deck)
      return self.deck
   
   def draw(self):
      self.deck.pop(0)
      return self.deck

        