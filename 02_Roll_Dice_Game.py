import random

# Conditions method
def conditions(dice_roll, number):
    if dice_roll == 1:
        print("You rolled a 1, you lose!") 
        return 0  # Reset the total to 0 if the user loses
    else: 
        number += dice_roll
        print("You rolled a", dice_roll, "your total is", number)
        return number

# Game logic
try_counter = 0
total = 0
print("Let's start the DICE ROLL GAME!")
while True:
    attempt = input("Would you like to roll? (y/n): ").lower()
    if attempt == "y":
        dice = random.randint(1, 6)  # Dice roll between 1 and 6
        print("You rolled a", dice)
        total = conditions(dice, total)  # Update the total based on the roll
        try_counter += 1  # Increment the roll counter
        print("Number of ATTEMPTS = ",try_counter)
    elif attempt == "n":
        print("Game over! You chose not to roll.")
        try_counter += 1  # Increment the roll counter
        print("Number of ATTEMPTS = ",try_counter)
    else:
        print("Invalid input. Please enter 'y' to roll or 'n' to quit.")
    
