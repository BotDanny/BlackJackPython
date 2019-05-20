# Global variable
from chips import Chips
from hand import Hand
from deck import Deck

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

def take_bet(chip):
    bet = 0
    print(f"You currently have ${chip.total}")
    while True:
        while True:
            try:
                bet = int(input("Please enter your bet: "))
            except:
                print("You did not enter a corrent integer")
            else:
                break
        if bet > chip.total:
            print("Your bet exceeds what you currently have")
        else:
            chip.take_bet(bet)
            print("You successfully made a bet")
            break
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    print(" ")
    print("Your ", end="")
    print(hand)
    print("Do you want to hit? enter 'y' for yes and anything else for no: ")
    ask = input("")
    if ask == "y":
        hand.add_card(deck)
        playing = True
    else:
        playing = False

def show_some(player,dealer):
    print(" ")
    print("The top card from the dealer is: ", end="")
    print(dealer.top_card())
    print("Your ", end="")
    print(player)
    print(" ")

def show_all(player,dealer):
    print(" ")
    print("Dealer's ", end="")
    print(dealer)
    print("Your ", end="")
    print(player)
    print(" ")

def main():
    global playing
    print("Welcome to Blackjack gambling!")
    print("You initial chip is $100")
    player_chip = Chips()
    while True:
        playing = True
        game_deck = Deck()
        game_deck.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_card(game_deck)
        player_hand.add_card(game_deck)
        dealer_hand.add_card(game_deck)
        dealer_hand.add_card(game_deck)
        show_some(player_hand,dealer_hand)
        take_bet(player_chip)
        while playing:
            if player_hand.value >= 21:
                break
            else:
                hit_or_stand(game_deck,player_hand)
        if player_hand.value > 21:
            show_all(player_hand,dealer_hand)
            player_chip.lose_bet()
            print(f"You busted! You lost your bet! Your new balance is: {player_chip.total}")
        elif player_hand.value == 21:
            show_all(player_hand,dealer_hand)
            player_chip.win_bet()
            print(f"Congradulation! You Won! Your new balance is: {player_chip.total}")
        else:
            print("Now is the dealer's turn, showing all cards")
            show_all(player_hand,dealer_hand)
            while dealer_hand.value < 17:
                dealer_hand.add_card(game_deck)
                print("The dealer has choosen to hit")
                show_all(player_hand,dealer_hand)
            if dealer_hand.value <= 21:
                print("The dealer has choosen to stand")
            if (dealer_hand.value > 21):
                player_chip.win_bet()
                print(f"The dealer has busted! You Won! Your new balance is: ${player_chip.total}")
            elif (dealer_hand.value < player_hand.value):
                player_chip.win_bet()
                print(f"The dealer is less than you! You won! Your new balance is: ${player_chip.total}")
            elif (dealer_hand.value == player_hand.value):
                player_chip.lose_bet()
                print(f"The dealer is the same as you! You lost! Your new balance is: ${player_chip.total}")
            else:
                player_chip.lose_bet()
                print(f"The dealer is more than you! You lost! Your new balance is: ${player_chip.total}")
        if player_chip.total == 0:
            print("You lost all your chip, quiting...")
            break
        print("Do you want to play another game? press 'y' for yes and anthing else for no")
        if input("") != 'y':
            print("You left the game with ${player_chip.total}")
            break
        print("Starting new game")
        print("------------------------------------------------------------------------------------------")

main()