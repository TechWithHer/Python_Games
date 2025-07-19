import random
from time import sleep

print("===== Welcome to the : GUESS THE NUMBER GAME =====")
sleep(3)
print("Rules:")
sleep(1)
print("1) You will provide a number range (start and end).")
print("2) A number will be randomly selected in that range.")
print("3) You need to guess the number.")
print("4) You'll be told if your guess is too low or too high.")
print("5) The game continues for 3 attempts, after 3rd attempt, the game terminates.")
print("6) Type any character anytime to quit the game.")
print("Let's begin!\n")

# ---- Get Valid Start Range ----     

def guess_number(num):
    i = 0
    while i < 3:
        i += 1
        guess = input("Enter your guess ")
        if guess.isdigit():
            guess = int(guess)
            if guess < num:
                print("Your guess is too low. Try again.")
            elif guess > num:
                print("Your guess is too high. Try again.")
            else:
                print("Congratulations! You've guessed the number correctly!")
                break
        else:
            print("Invalid input. Please enter a valid number or 'q' to quit.")
           
    if i == 3:
        print("The number was:", num)
        print("Thanks for playing! Your attempts are exhausted now. Goodbye!")
           


top_of_range = input("Enter the START OF THE RANGE (must be a number >= 0): ")
end_of_range = input("Enter the END of the range (must be greater than START OF THE RANGE): ")
if top_of_range.isdigit() and (int(top_of_range) >= 0) and end_of_range.isdigit() and (int(end_of_range) > int(top_of_range)):
    top_of_range = int(top_of_range)
    end_of_range = int(end_of_range)
else:
         print("Invalid input. Please enter a valid range.")
num = random.randint(int(top_of_range), int(end_of_range))
guess_number(num)