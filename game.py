"""
@author: sarvar umurzakov
"""

""" Importing random module """
import random

""" main function that is responsible for starting, selecting and ending the game """
def main():
    suits = {
        1: "Clubs",
        2: "Spades",
        3: "Diamonds",
        4: "Hearts"
    }
    values = {val: str(val) for val in range(2, 11)}
    values[1] = "Ace"
    values[11] = "Jack"
    values[12] = "Queen"
    values[13] = "King"

    while True:
        choice = input("\nSelect which game you want to play, enter 1 or 2.\n1. Game of War\n2. Game of Life N Death\n> ")
        if(choice != "1" and choice != "2"):
            print("Invalid input!")
            continue
        break

    while True:
        try:
            num_cards = int(input("How many cards do you want to deal? "))
            if num_cards <= 0 or num_cards > 26:
                raise Exception
            break
        except:
            print("Invalid input!")

    if choice == "1":
        my_deck = shuffle_deck(create_deck())
        p1, p2 = deal(my_deck, num_cards)
        play_war(p1, p2, suits, values)
    elif choice == "2":
        while True:
            try:
                totLen = int(input("What is the size of the winning hand ?"))
                if(num_cards > totLen or totLen > 52):
                    raise Exception
                break
            except:
                print("Invalid input")
        my_deck = shuffle_deck(create_deck())
        p1, p2 = deal(my_deck, num_cards)
        play_lifeNdeath(p1, p2, my_deck, suits, values, totLen)


""" func create_deck() creates deck of cards and returns list of tuples (suit,value) """
def create_deck():
    suits = {
        1: "Clubs",
        2: "Spades",
        3: "Diamonds",
        4: "Hearts"
    }
    values = {val: str(val) for val in range(2, 11)}
    values[1] = "Ace"
    values[11] = "Jack"
    values[12] = "Queen"
    values[13] = "King"

    return [(suit, val) for suit in suits.values() for val in values.values()]


""" func shuffle_deck(deck) takes deck, list of tuples and returns shuffled deck"""
def shuffle_deck(deck):
    new_deck = list(deck)
    random.shuffle(new_deck)
    return new_deck


""" func print_deck(deck, suits, values) takes deck, suits, values as argument and print player's cards as tuple """
def print_deck(deck, suits, values):
    strValue = ""
    for iter in deck:
            strValue += "(" + str(iter[0]) + ":" + str(iter[1]) + ")"
    print(strValue)


""" func deal(deck, num_cards) takes deck, num_cards as arguments and returns tuple where first element is 
    the first player's cards and second element is the second player's card.
"""
def deal(deck, num_cards):
    theFirstList = []
    new_deck = list(deck)
    for val in range(num_cards):
        item = random.choice(new_deck)
        theFirstList.append(item)
        new_deck.remove(item)
    theSecondList = []
    for val in range(num_cards):
        item = random.choice(new_deck)
        theSecondList.append(item)
        new_deck.remove(item)
    # print(set(theFirstList).intersection(theSecondList))
    return theFirstList, theSecondList


def get_key_by_values(value, my_dict):
    for key, val in my_dict.items():
        if value == val:
            return key
    return -1

""" func play_war takes p1, p2, suits, values as arguments. p1, p2 is list of tuples, suits and values are dictionary.
    Method starts the play war game """
def play_war(p1, p2, suits, values):
    print("\nPlayer 1's hand:")
    print_deck(p1, suits, values)
    print("\nPlayer 2's hand:")
    print_deck(p2, suits, values)
    print("\nStart>>")

    first, second = 0, 0
    for val in range(len(p1)):
        print("Player 1:  " + str(p1[val][0]) + " " + str(p1[val][1]))
        print("Player 2:  " + str(p2[val][0]) + " " + str(p2[val][1]))

        val_one = get_key_by_values(p1[val][1], values)
        val_two = get_key_by_values(p2[val][1], values)

        if val_one > val_two:
            first += 1
        elif val_two > val_one:
            second += 1

        print("Scores>> Player 1: " + str(first) + ", Player 2: " + str(second))
    if(first == second):
        print("\nThere is no winner, draw.")
        return
    if(first > second):
        print("\nThe winner of this round is Player 1 with " + str(first) + " points.")
    else:
        print("\nThe winner of this round is Player 2 with " + str(second) + " points.")

""" func play_lifeNdeath takes p1, p2, deck, suits, values, totLen as arguments and start play life and death game. """
def play_lifeNdeath(p1, p2, deck, suits, values, totLen):
    print("\nPlayer 1's hand:")
    print_deck(p1, suits, values)
    print("\nPlayer 2's hand:")
    print_deck(p2, suits, values)
    print("\nStart>>")

    for i in range(50):
        print("Player 1:  " + str(p1[0][0]) + " " + str(p1[0][1]))
        print("Player 2:  " + str(p2[0][0]) + " " + str(p2[0][1]))
        first = get_key_by_values(p1[0][1], values)
        second = get_key_by_values(p2[0][1], values)

        item1 = p1.pop(0)
        item2 = p2.pop(0)

        if first > second:
            p1.append(item1)
            p1.append(item2)
        elif second > first:
            p2.append(item2)
            p2.append(item1)


        print("P1's hand")
        print_deck(p1, suits, values)
        print("P2's hand")
        print_deck(p2, suits, values)

        if(len(p1) == totLen):
            print("\nThe winner of Life N Death game is Player 1. Total round played: " + str(i + 1))
            return
        elif(len(p2) == totLen):
            print("\nThe winner of Life N Death game is Player 2. Total round played: " + str(i + 1))
            return
    if(len(p1) > len(p2)):
        print("\nThe winner of Life N Death game is Player 1. Total round played: 50")
    elif(len(p2) > len(p1)):
        print("\nThe winner of Life N Death game is Player 2. Total round played: 50")
    else:
        print("\nThere is no winner, it is draw")


""" Running game """
main()











