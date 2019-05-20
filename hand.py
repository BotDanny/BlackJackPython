from deck import Deck

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        dealt_card = card.deal()
        self.cards.append(dealt_card)
        if dealt_card.rank == "Ace":
            if self.value <= 10:
                self.value += 11
            else:
                self.value += 1
        else:
            self.value += values[dealt_card.rank]

    def __str__(self):
        flat_deck = [str(card) for card in self.cards]
        return "Current hand is: " + str(flat_deck) + f", Current value is {self.value}"

    def top_card(self):
        return "[" + str(self.cards[-1]) + "]"