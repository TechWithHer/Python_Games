# 🎮 Python_Games

A collection of 7 beginner-friendly yet intelligent Python mini-games bundled with a central game launcher. This project is designed to boost Python fundamentals, problem-solving, and API integration skills. Great for beginners, students, and aspiring developers.

---

## 📦 Included Games

| Game No | File Name                          | Description |
|--------:|------------------------------------|-------------|
| 01      | `01_Guess_Number_Game.py`          | A classic number guessing game. The computer selects a random number; the player tries to guess it in minimal attempts. |
| 02      | `02_Roll_Dice_Game.py`             | Simulates rolling a 6-sided dice. Displays the result using ASCII art. |
| 03      | `03_Stone_Paper_Scissors_Game.py`  | Traditional Rock, Paper, Scissors game where you play against the computer. |
| 04      | `04_Maths_Quiz_Game.py`            | A fun quiz that asks randomized arithmetic questions with a scoring mechanism. |
| 05      | `05_Password_Generator.py`         | Generates strong, secure passwords based on user preferences for length and character types. |
| 06      | `06_Madlibs_Game.py`               | Fill-in-the-blank style storytelling game using `story.txt` as a template. Makes funny or creative stories. |
| 07      | `07_Guess_Country_Game.py`         | API-powered game that gives you clues (capital, currency, population) and lets you guess the country. Uses the REST Countries API. |

---

## 🚀 How to Play

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/Python_Games.git
   cd Python_Games
Install Required Packages
Only one game requires an external library:

bash
Copy
Edit
pip install requests
Run the Main Game Launcher

bash
Copy
Edit
python Main_Python_Games.py
You'll be prompted with a menu to select any game.

📁 Project Structure
bash
Copy
Edit
Python_Games/
├── 01_Guess_Number_Game.py
├── 02_Roll_Dice_Game.py
├── 03_Stone_Paper_Scissors_Game.py
├── 04_Maths_Quiz_Game.py
├── 05_Password_Generator.py
├── 06_Madlibs_Game.py
├── 07_Guess_Country_Game.py
├── Main_Python_Games.py         # Master launcher file
├── story.txt                    # Used by Madlibs game
└── README.md                    # You're reading it!
💡 Key Highlights
🎯 Interactive and logic-based Python games

🌐 Real-time API integration (REST Countries API)

🧩 Great for learning conditionals, loops, I/O, and data handling

💡 Ideal for beginners or coding practice sessions

🧭 Easy to extend with new games via Main_Python_Games.py

🛠 Technologies Used
Python 3.6+

random, time, sys, os – from the standard library

requests – for live API data in the country guessing game

Basic file I/O (story.txt)

🔧 Requirements
Python 3.6 or later

Terminal / Command Prompt / IDE (VSCode, PyCharm, etc.)

Internet connection (only for Game 07)

🧪 How to Contribute
Want to add your own Python game?

Fork the repository

Create a new game file (08_Hangman_Game.py, for example)

Add it to Main_Python_Games.py menu logic

Submit a pull request 🎉

📄 License
This project is open-source and available under the MIT License.
