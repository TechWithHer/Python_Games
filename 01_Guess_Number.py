import random

print("===== GUESS THE NUMBER GAME =====")
print("Welcome to the game!")
print("Rules:")
print("1) You will provide a number range (start and end).")
print("2) A number will be randomly selected in that range.")
print("3) You need to guess the number.")
print("4) You'll be told if your guess is too low or too high.")
print("5) The game continues until you guess it correctly.")
print("6) Type 'q' anytime to quit the game.")
print("Let's begin!\n")

# ---- Get Valid Start Range ----
while True:
    top_of_range = input("Enter the START of the range (must be a number >= 0): ")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        break
    else:
        print("Invalid input. Please enter a valid number.")

# ---- Get Valid End Range ----
while True:
    end_of_range = input("Enter the END of the range (must be greater than start): ")
    if end_of_range.isdigit() and int(end_of_range) > top_of_range:
        end_of_range = int(end_of_range)
        break
    else:
        print("Invalid input. End must be a number greater than start.")

# ---- Secret Number ----
secret_number = random.randint(top_of_range, end_of_range)
guess_count = 0

# ---- Guessing Loop ----
while True:
    guess = input(f"Guess a number between {top_of_range} and {end_of_range}: ")

    if guess.lower() == 'q':
        print("You chose to quit the game. Goodbye!")
        break

    if not guess.isdigit():
        print("Invalid guess. Please enter a number or 'q' to quit.")
        continue

    guess = int(guess)
    guess_count += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed the correct number: {secret_number}")
        print(f"It took you {guess_count} guesses.")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
