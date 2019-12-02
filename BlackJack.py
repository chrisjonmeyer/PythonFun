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

# Create a Chips Class to managae player's chip values
class Chips():
    
    def __init__(self):
        self.total = 100  # This is a pre-set value, but it can be supplied by the user in the future
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

# Function Definitions
def take_bet():
    while True:
        try:
            player_bet = int(input("How much would you like to bet?"))
        except: 
            print("Not a valid bet")
            continue
        else:
            break
    return player_bet

def hit(deck,hand):
    hit_card = deck.deal()
    hand.add_card(hit_card)
    print("Hit ", hit_card, " ", hand.value)

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        player_response = input("Do you want to Hit?")
        if (player_response == 'Yes'):
            hit(deck,hand)
        else:
            print("Standing with ", hand.value)
            playing = False
            break

def show_some(player,dealer):
    print("Dealer's Hand:")
    print(dealer.cards[0])
    print("Hidden Card\n")
    print("Player's Hand:", player.value)
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    print("Dealer's Hand: ", dealer.value)
    for card in dealer.cards:
        print(card)
    print("\nPlayer's Hand: ", player.value)
    for card in player.cards:
        print(card)

# End of Game Scenarios  - Need to populate these mroe
def player_busts():
    print("Player Busts")

def player_wins():
    print("Player Wins")

def dealer_busts():
    print("Dealer Busts")

def dealer_wins():
    print("Dealer Wins")

def push():
    print("Push")


# Testing Section 
#card1 = Card("Hearts","Three")
#print(card1)
# deck1 = Deck()
# deck1.shuffle()
#print(deck1)
# player1 = Hand()
# player1.add_card(deck1.deal())
# player1.add_card(deck1.deal())
# dealer1 = Hand()
# dealer1.add_card(deck1.deal())
# dealer1.add_card(deck1.deal())
# for card in player1.cards:
#     print(card)
# print(player1.value)
# show_all(player1,dealer1)

# The actual game!

while True:
    print("Welcome to the BlackJack Table")
    # Creating/Shuffling the deck
    print("Shuffling the deck")
    main_deck = Deck()
    main_deck.shuffle()
    # Dealing cards to player and dealer
    player = Hand()
    dealer = Hand()
    player.add_card(main_deck.deal())
    player.add_card(main_deck.deal())
    dealer.add_card(main_deck.deal())
    dealer.add_card(main_deck.deal())
    player_bet = input("How much would you like to bet?")
    show_some(player,dealer)
    hit_or_stand(main_deck,player)
    break
    