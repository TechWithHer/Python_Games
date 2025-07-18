import random
import string
from colorama import init, Fore, Style

# Initialize colorama (needed for Windows terminal support)
init(autoreset=True)

def generate_password(length, use_special, use_numbers):
    print(Fore.CYAN + "\n🔐 Let me suggest a strong password for you...\n")

    # Character sets
    characters = string.ascii_letters
    if use_special:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits

    if not characters:
        print(Fore.RED + "⚠️ No characters selected! Cannot generate password.")
        return ""

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_yes_no(prompt):
    """Ask yes/no and return True/False"""
    while True:
        answer = input(Fore.YELLOW + prompt + " (Y/N): ").strip().lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print(Fore.RED + "Please enter 'Y' or 'N'.")

def main():
    print(Fore.MAGENTA + Style.BRIGHT + "\n" + "="*40)
    print("🧠 Welcome to the Smart Password Generator!")
    print("="*40 + Style.RESET_ALL)

    # Ask password length
    while True:
        try:
            length = int(input(Fore.GREEN + "\n🔢 Enter the desired password length: "))
            if length > 0:
                break
            else:
                print(Fore.RED + "Please enter a number greater than 0.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

    # Ask for character types
    use_special = get_yes_no("Do you want special characters?")
    use_numbers = get_yes_no("Do you want numbers?")

    # Generate and show password
    password = generate_password(length, use_special, use_numbers)
    if password:
        print(Fore.CYAN + "\n✅ Your generated password is:\n")
        print(Fore.GREEN + Style.BRIGHT + f"{'*' * (length + 4)}")
        print(Fore.YELLOW + Style.BRIGHT + f"* {password} *")
        print(Fore.GREEN + Style.BRIGHT + f"{'*' * (length + 4)}\n")

if __name__ == "__main__":
    main()
