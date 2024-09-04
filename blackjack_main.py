
import art
import random as rd

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_cards(bot):
    """ Draws cards from the given card list and returns a list called hand"""
    hand = []

    for i in range (2):
        dealt = rd.choice(cards)
        hand.append(dealt)
    dealer = True
    if dealer == bot:
        while 16>sum(hand)<21:
            dealt = rd.choice(cards)
            hand.append(dealt)

    # to work on ... the user must fetch the damn deck & return a respond if he wants to hit or stand
    if dealer != bot:
        rep = True
        while rep:
            if sum(hand)<21:
                add = input("Do you want another card? (Hit) Yes[y] or (Stand) No?[n]: ")
                if add == "y":
                    hit = rd.choice(cards)
                    hand.append(hit)
                    print("-"*80)
                    print(f"Here is another card: {hit} \nYour current hand is: {hand}")
                    rep = True
                elif add == "n":
                    print(f"Your current hand is: {hand}")
                    rep = False
            else:
                print("Hmmm none of the above choices ... continuing for now...")
            
    if sum(hand)>21 and 11 in hand:
        hand[hand.index(11)] = 1
    
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

restart = True
while restart:
    print(art.logo)
    print("="*80)


    dealer = draw_cards(bot=True)
    mul = len(dealer)-1
    print(f"Dealers Cards: {dealer[0]}","[_]"*mul)
    dealer_hands = sum(dealer)

    player = draw_cards(bot=False)
    print(f"Player Cards: {player}")
    players_hands = sum(player)
    print(f"Player's Hand: {players_hands}")
       
    check_both_hands(dealer_hands,players_hands)
    print(f"Player's Hand: {dealer}")


    q = input("Want to play again? Type any letter to play another round, press [n] to Exit:\n")
    if q == "n":
        restart = False
    else: 
        print("\n"*20)
        print(art.logo)
        print("Shuffling cards for another round ...")
 

