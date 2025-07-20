import random
from time import sleep
import string

# Game Introduction
print("🎉 Welcome to PASSWORD GENERATION!")
print("You will enter a desired length, and we'll generate a strong password for you.")
sleep(2)

def get_character_pool():
    use_special = input("Do you want special characters in the password? (y/n): ")
    use_numbers = input("Do you want numbers in the password? (y/n): ")
    
    characters = string.ascii_letters  # always include letters

    if use_special.lower() == "y":
        characters += string.punctuation
    elif use_special.lower() != "n":
        print("Invalid input for special characters. Defaulting to letters only.")

    if use_numbers.lower() == "y":
        characters += string.digits
    elif use_numbers.lower() != "n":
        print("Invalid input for numbers. Defaulting to letters only.")

    return characters

# --------------------------
try:
    length = int(input("\n🔢 Enter the desired password length: "))
    if length <= 0:
        print("❌ Please enter a valid positive number.")
    else:
        char_pool = get_character_pool()
        password = ''.join(random.choice(char_pool) for _ in range(length))
        print("\n🔐 The Generated Password is:", password)
except ValueError:
    print("❌ Please enter a numeric value for length.")
