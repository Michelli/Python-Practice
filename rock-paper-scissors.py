import random

player_one = str(input("Rock, paper, or scissors? ")).lower()

def game(one):
    hands = ["rock", "paper", "scissors"]
    two = hands[random.randint(0,2)]

    if one in hands:
        print(f"You chose {one}.\nI picked {two}.\n")

        if one == two:
            print("It's a tie!\n")
        elif (one == "rock" and two == "scissors") or (one == "paper" and two == "rock") or (one == "scissors" and two == "paper"):
            print("You win!\n")
        else:
            print("You lose!\n")
        
    else:
        print("That's not a valid option.\n")

game(player_one)