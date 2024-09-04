
import art
import random as rd
import cards as c
import player_draw as pd

def cards():
    dealer_cards = [] 
    for i in range(2):
        dealt = rd.choice(c.cards)
        dealer_cards.append(dealt)
    if sum(dealer_cards)<16:
        dealt = rd.choice(c.cards)
        dealer_cards.append(dealt)
    # print(dealer_cards)
    return dealer_cards


def computer_hand(dealt = []):
    hand = sum(dealt)
    if hand>21:
        print("Dealer's a Bust")
        return hand
    else:
        return hand
    
def check_both_hands(com_hand, pos_hand):
    if pos_hand<com_hand<21:
        print("Dealer Wins")
    elif com_hand<pos_hand<21:
        print("Player Wins")
    elif com_hand == pos_hand:
        print("Both players & dealer won. It is a draw!")
    elif com_hand == 21:
        print("BlackJack! Dealer Wins")
    elif pos_hand == 21:
        print("BlackJack! Player Wins")
    elif com_hand> 21:
        print("Dealer Bust: Player wins")
    elif pos_hand> 21:
        print("Player Bust: Dealer wins")
    
    

print(art.logo)

restart = True
while restart:
    hidden_cards = len(cards())-1 
    print(f"Dealer shows first card: [{cards()[0]}]","[]"*hidden_cards)
    print("="*80)

    dealer = computer_hand(cards())
    player = pd.player_hand()
    
    check_both_hands(dealer, player)

    print(f"Dealer's Cards are: {cards()}")

    q = input("Want to play again? Type any letter to play another round, press [n] to Exit:\n")
    if q == "n":
        restart = False
    else: 
        print("\n"*20)
        print(art.logo)
        print("Shuffling cards for another round ...")
 

