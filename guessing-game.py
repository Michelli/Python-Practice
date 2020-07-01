import random

random_num = random.randint(1,50)
input_num = 0
running_count = 0

while input_num != random_num:
    input_num = int(input("Guess: "))
    running_count += 1

    if input_num == random_num:
        print(f"Correct! It took you {running_count} attempts.")
        break
    elif input_num < random_num:
        print("Too low!\n")
        continue
    else:
        print("Too high!\n")
        continue