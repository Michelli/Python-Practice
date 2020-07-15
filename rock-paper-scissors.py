import random

hands = ["rock", "paper", "scissors"]

def player_one():
    one = "Spock"

    while one not in hands:
        one = str(input("Rock, paper, or scissors? ")).lower()
        if one not in hands:
            print("That's not a valid option.\n")
        else:
            return one

def game(one):
    two = hands[random.randint(0,2)]

    if one in hands:
        print(f"You chose {one}.\nI picked {two}.\n")

        if one == two:
            print("It's a tie!\n")
        elif (one == "rock" and two == "scissors") or (one == "paper" and two == "rock") or (one == "scissors" and two == "paper"):
            print("You win!\n")
        else:
            print("You lose!\n")
        
game(player_one())