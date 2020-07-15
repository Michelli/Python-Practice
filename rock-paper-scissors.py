import random

hands = ["rock", "paper", "scissors"]
play_game = True

def player_one():
    # Lizard poisons Spock
    one = "Spock"

    # Keep asking the user for input unless valid
    while one not in hands:
        one = input("Rock, paper, or scissors? ").lower()

        # Error message
        if one not in hands:
            print("That's not a valid option.\n")
    
    return one

def game(one):
    # Generate the CPU's hand
    two = hands[random.randint(0,2)]

    # Let user know what the CPU has chosen
    print(f"You chose {one}.\nI picked {two}.\n")

    # The actual game logic
    if one == two:
        print("It's a tie!\n")
    elif (one == "rock" and two == "scissors") or (one == "paper" and two == "rock") or (one == "scissors" and two == "paper"):
        print("You win!\n")
    else:
        print("You lose!\n")

def continue_playing():
    continue_game = "unknown"
    options = ["y", "n"]

    # Keep asking the user for input unless valid
    while continue_game not in options:
        continue_game = input("Continue playing? (Y or N) ").lower()

        # Error message
        if continue_game not in options:
            print("I don't understand.")

    if continue_game == "y":
        return True
    else:
        return False
        
while play_game:
    # Prompt user for hand
    one = player_one()

    # Play game
    game(one)

    # Ask if player wants to continue
    play_game = continue_playing()