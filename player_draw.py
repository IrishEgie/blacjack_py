import random as rd
import cards as c

def player_hand():
    hand = 0
    for rep in range (2):
        dealt = rd.choice(c.cards)
        print(f"Here are your cards: {dealt}")
        hand+=dealt
    print(f"Your current hand is: {hand}")
    print("="*80)

    rep = True
    while rep:
        if hand<21:
            add = input("Do you want another card? (Hit) Yes[y] or (Stand) No?[n]: ")
            if add == "y":
                hit = rd.choice(c.cards)
                hand += hit
                print("-"*80)
                print(f"Here is another card: {hit} \nYour current hand is: {hand}")
                rep = True
            elif add == "n":
                print(f"Your current hand is: {hand}")
                rep = False
                return hand
        elif hand==21:
            print("BlackJack You win!")
            return hand
        elif hand>21:
            print(f"Busted!")
            return hand

        else:
            print("Hmmm none of the above choices ... ending game for now...")
            return hand

        
            
        

