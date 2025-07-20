import os

def show_menu():
    print("\n🎮 Welcome to Python Game Launcher 🎮")
    print("Select a game to play:")
    print("1. GUESS THE NUMBER GAME 🔢")
    print("2. ROLL THE DICE GAME 🎲")
    print("3. STONE, PAPER & SCISSOR GAME")
    print("4. MATHS QUIZ GAME ❌⭕")
    print("5. Password Generator 🔐")
    print("6. MADLIBS GAME ⌨️")
    print("7. GUESS THE COUNTRY GAME 🧩")
    print("0. Exit 🚪")

def launch_game(choice):
    game_files = {
        "1": "01_Guess_Number_Game.py",
        "2": "02_Roll_Dice_Game.py",
        "3": "03_Stone_Paper_Scissors_Game.py",
        "4": "04_Maths_Quiz_Game.py",
        "5": "05_Password_Generator.py",
        "6": "06_Madlibs_Game.py",
        "7": "07_Guess_Country_Game.py"
    }

    if choice in game_files:
        os.system(f"python3 {game_files[choice]}")
    elif choice == "0":
        print("Exiting. Bye! 👋")
        exit()
    else:
        print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    while True:
        show_menu()
        user_choice = input("Enter your choice: ")
        launch_game(user_choice)
