
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
        
    if sum(hand)>21 and 11 in hand:
        hand[hand.index(11)] = 1
    
    return hand
def player_cards (hand):
    hand

    while sum(hand)<21:
        print("-"*80)
        add = input("Do you want another card? (Hit) Yes[y] or (Stand) No?[n]: ").lower()
        if add == "y":
            hit = rd.choice(cards)
            hand.append(hit)
            print("-"*80)
            print(f"Here is another card: {hit} \nYour current hand is: {sum(hand)}, your cards are: {hand}")                
        elif add == "n":
            print(f"Your current hand is: {sum(hand)}, your cards are: {hand}")
            return hand        
    if sum(hand)==21:
        print(f"Your current hand is: {sum(hand)}, your cards are: {hand}")
    elif sum(hand)>21:
        print(f"Your current hand is: {sum(hand)}, BUST!")
    else:
        print("Hmmm none of the above choices ... continuing for now...")
    return hand 
        
def check_both_hands(com_hand, pos_hand):
    if pos_hand<com_hand:
        if com_hand<21:
            print("Dealer Wins")
        elif com_hand == 21:
            print("BlackJack! DEALER Wins")
        else:
            print("Dealer Bust: PLAYER wins")
    elif com_hand<pos_hand:
        if pos_hand<21:
            print("Player Wins")
        elif pos_hand == 21:
            print("BlackJack! PLAYER Wins")
        else:
            print("Player Bust: DEALER wins")
    elif com_hand and pos_hand > 21:
        print("Both players & dealer BUST. It is a DRAW!")
    elif com_hand == pos_hand:
        print("Both players & dealer WON. It is a DRAW!")


    
    print("-"*80)
restart = True
while restart:
    print(art.logo)
    print("="*80)

    #dealer block
    dealer = draw_cards(bot=True)
    mul = len(dealer)-1
    print(f"Dealers Cards: {dealer[0]}","[_] "*mul)
    dealer_hands = sum(dealer)

    #player block
    player = draw_cards(bot=False)
    print(f"Player Cards: {player}")
    player_cards(player)
    print(f"Player's Hand: {sum(player)}")

    #result
    print("-"*80)
    print(f"Dealers Cards: {dealer}")
    print(f"Dealers's Hand: {dealer_hands}")
    #check both the player's & the dealer's Cards
    print("="*80)
    check_both_hands(dealer_hands,sum(player))

    print("="*80)
    q = input("Want to play again? Type any letter to play another round, press [n] to Exit:\n")
    
    if q == "n":
        restart = False
        print("Thank you for Playing PyBlackJack! ...")
    else: 
        print("\n"*20)
        print(art.logo)
        print("Shuffling cards for another round ...")
 

