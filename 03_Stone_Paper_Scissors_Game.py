import random
from time import sleep

# Game introduction
print("===== Welcome to the : STONE, PAPER & SCISSOR GAME =====")
sleep(3)
print("Rules:")
sleep(1)
print("1) You will be playing against Computer")
print("2) Stone beats Scissors, Scissors beats Paper, and Paper beats Stone.")
print("3) Game with continue in the loop unless you stop it or enter invalid input")
name = input("Please enter your name: ")
sleep(3)    

#define a method game_logic
def game_logic(player, comp):
 if (player == "stone" or player == "s") and (comp == "scissors"):
  print("You won!")
 elif (player == "paper" or player == "p") and comp == "stone":
  print("You won!") 
 elif (player == "scissors" or player == "x") and comp == "paper":
  print("You won!")
 elif player == comp:
  print("It's a tie!")
 else:
  print("You lost!")
   
#define a method of play_again
def play_again(again):
  again = input("WANNA PLAY AGAIN? y/n " )
  if again == "n":
    print("Game terminted, bye")
    quit()
  elif again == "y": 
    print("Let's play again!") 
    return True
  else:
    print("Invalid input")
    return play_again()

    
#actual code begins here
print("Hi " + str(name) + " Let's start the game!")
a = 0
options = ["stone","paper","scissors","s","p","x"]
while True:
  Player_Input= input("Enter anything out of Stone(or S), Paper(or P) OR Scissors(or X)  ")
  if Player_Input.lower() in options:
    comp_choice = random.choice(options[0:3])
    print("Computer's choice is " + str(comp_choice))
    game_logic(Player_Input, comp_choice)
    play_again(a)
  else:
   print("Your entry is incorrect")
   print("Game terminted, bye")
   break


  


  



  
