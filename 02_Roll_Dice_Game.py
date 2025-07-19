import random
from time import sleep

# Game introduction
print("===== Welcome to the : ROLL THE DICE GAME =====")
sleep(3)
print("Rules:")
sleep(1)
print("1) You will be playing against Computer")
print("2) There will be 3 attempts to roll the dice.")
print("3) We will sum up all the rolls.")
print("4) One with the highest total wins.")
name = input("Please enter your name: ")
sleep(3)    

# Function to handle user action
def user_action():
    q = input("Press Enter to roll the dice...")
    if q != "":
        print("Invalid input. Chance lost. Please just press Enter to roll the dice.")
        return 0  # Return 0 if invalid input
    else:
        return random.randint(1, 6)  # Return a random dice roll
    
def the_game(count_name, count_computer):
    for attempt in range(3):
        print(f"Attempt {attempt + 1}:")
        sleep(1)
        print(f"{name}'s turn to roll the dice.")
        sleep(1)   
        user_roll = user_action()  # Get the user's dice roll
        if user_roll == 0:  # Check for invalid input
            continue
        print(f"{name} rolled: {user_roll}")
        sleep(1)
        print("Now it's the computer's turn.")
        sleep(1)
        computer_roll = random.randint(1, 6)  # Computer rolls the dice
        print(f"Computer rolled: {computer_roll}")
        sleep(2)
        count_name += user_roll
        count_computer += computer_roll
    sleep(1)
    print(f"Final Scores: {name}: {count_name}, Computer: {count_computer}")
    sleep(1)
    
    if count_name > count_computer:
        print(f"{name} wins this round!")
    elif count_name < count_computer:
        print("Computer wins this round!")
    else:
        print("It's a tie!")

# Main Program
print("Let's start the game, ", name, " Vs COMPUTER")
counter_user = 0  # User's total score
counter_computer = 0  # Computer's total score
the_game(counter_user, counter_computer)
sleep(2)
print("Thank you for playing the Roll the Dice Game!")