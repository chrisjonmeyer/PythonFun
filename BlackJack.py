# Create a BlackJack game via python.

import random

# Declare the variables to store suits, ranks, and values
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

# Card Class - Has two attributes suit and rank.
class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
         return f"{self.rank} of {self.suit}"

# Deck Class - Ceates a deck of 52 cards on init. Is able to shuffle and deal. 
class Deck:

    def __init__(self):
        self.deck = []  #Start with an empty deck
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

# Create a Hand Class
class Hand():
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Create a Chips Class
class Chips():
    
    def __init__(self):
        


# Testing Section
card1 = Card("Hearts","Three")
#print(card1)
deck1 = Deck()
deck1.shuffle()
#print(deck1)
player1 = Hand()
player1.add_card(deck1.deal())
player1.add_card(deck1.deal())
for card in player1.cards:
    print(card)
print(player1.value)