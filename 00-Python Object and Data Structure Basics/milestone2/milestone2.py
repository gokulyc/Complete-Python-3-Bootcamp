# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '00-Python Object and Data Structure Basics'))
	print(os.getcwd())
except:
	pass
# %%
from IPython import get_ipython
# %%
import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
playing=True


# %%
class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return self.rank+" of "+self.suit
# print(__name__)


# %%
class Deck():
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return "The Deck has : "+deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card

# %% [markdown]
# **Testing above classes :**

# %%
test_deck=Deck()
test_deck.shuffle()
print('deal one card !!! :',test_deck.deal())
print(test_deck)


# %%
class Hand():
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces +=1
    
    def adjust_for_ace(self):
        # If Total Value > 21 and i still have an ace
        # Than Change My Ace to be a 1 instead of an 11
        while self.value>21 and self.aces>0:
            self.value -= 10
            self.aces -=1


# %%
test_deck=Deck()
test_deck.shuffle()


# %%
# Player
test_player = Hand()
pulled_card=test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)


# %%
class Chips():

    def __init__(self,total=100):
        self.total=total
        self.bet=0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# %%
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would like to bet? "))
        except:
            print("Please provide integer.")
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips! you have : {}'.format(chips.total))
            else:
                break


# %%
def hit(deck,hand):
    single_card=deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


# %%
def hit_or_stand(deck,hand):
    global playing
    while True:
        x=input('Hit or Stand? Enter h or s :')
        if x[0].lower()=='h':
            hit(deck,hand)
        elif x[0].lower()=='s':
            print("Player Stands Dealer's Turn")
            playing= False
        else:
            print("Sorry, I did not understand that, please enter h or s only!")
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
# %%
def player_busts(player,dealer,chips):
    print("Bust Player ! ")
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print('Player Wins!')
    chips.win_bet()
def dealer_busts(player,dealer,chips):
    print('Player Wins! Dealer Busted!')
    chips.win_bet()
def dealer_wins(player,dealer,chips):
    print("Bust Player!")
    chips.lose_bet()

def push(player,dealer):
    print('Dealer and Player tie! Push')

# %% [markdown]
# ** Game Main Initilization **

# %%
while True:
    # print opening statement
    print("Welcome to BlackJack")
    # Create & Shuffle the deck ,deal two cards to each other player
    deck=Deck()
    deck.shuffle()
    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    # set up the player's chips 
    player_chips=Chips()

    # prompt the player for their bet 
    take_bet(player_chips)
    # show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    while playing: # recall this variable from our hit_or_stand function
        hit_or_stand(deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    if player_hand.value<=21:

        while dealer_hand.value<17:
            hit(deck,dealer_hand)
        show_all(player_hand,dealer_hand)

        if dealer_hand.value>21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value<player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    print('\n Player total chips are at: {}'.format(player_chips.total))
    new_game = input("Would you like to play another game? y/n :")

    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print('Thank you for playing!')
        break
