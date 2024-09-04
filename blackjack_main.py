import art
import random as rd

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_cards(bot):
    """Draws cards and returns a hand."""
    hand = [rd.choice(cards) for _ in range(2)]

    while bot and 16 > sum(hand) < 21:
        hand.append(rd.choice(cards))
    
    if sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
    
    return hand

def player_cards(hand):
    """Handles player's card drawing."""
    while sum(hand) < 21:
        print("-" * 80)
        add = input("Do you want another card? (Hit) Yes[y] or (Stand) No?[n]: ").lower()

        if add == "y":
            hand.append(rd.choice(cards))
            print(f"Here is another card. Your current hand is: {sum(hand)}, your cards are: {hand}")
        elif add == "n":
            break
        else:
            print("Invalid choice, continuing...")

    result = "BUST!" if sum(hand) > 21 else f"Your final hand is: {sum(hand)}"
    print(f"{result}, your cards are: {hand}")
    
    return hand
        
def check_both_hands(com_hand, pos_hand):
    """Compares hands and prints the result."""
    if com_hand == pos_hand:
        result = "DRAW!"
    elif pos_hand > 21 or (com_hand <= 21 and com_hand > pos_hand):
        result = "Dealer Wins"
    else:
        result = "Player Wins"

    result += " (Blackjack!)" if 21 in [com_hand, pos_hand] else ""
    result += " (Both BUSTED!)" if com_hand > 21 and pos_hand > 21 else ""
    print(result)

# Game loop
restart = True
while restart:
    print(art.logo)
    print("=" * 80)

    # Dealer's turn
    dealer = draw_cards(bot=True)
    print(f"Dealer's Cards: {dealer[0]} {'[_] ' * (len(dealer) - 1)}")
    
    # Player's turn
    player = draw_cards(bot=False)
    print(f"Player's Cards: {player}")
    player_cards(player)

    # Show results
    print("-" * 80)
    print(f"Dealer's Cards: {dealer}")
    print(f"Dealer's Hand: {sum(dealer)}")
    print(f"Player's Hand: {sum(player)}")
    check_both_hands(sum(dealer), sum(player))

    # Ask for a restart
    restart = input("Want to play again? Press [n] to exit, any other key to continue: ").lower() != "n"
    if restart:
        print("\n" * 3 + "Shuffling cards for another round...")

print("Thank you for Playing PyBlackJack!")
