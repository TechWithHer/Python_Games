import random

#define a method game_logic
def game_logic(player, comp):
 if player == "stone" and comp == "scissors":
  print("You have won!")
 elif player == "paper" and comp == "stone":
  print("You have won!") 
 elif player == "scissors" and comp == "paper":
  print("You have won!")
 elif player == comp:
  print("It's a tie!")
 else:
  print("You have lost!")
   
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
 
a = 0
Player_Name= input("To start, please enter your name.  ")
options = ["stone", "paper", "scissors"]
print("Hi " + str(Player_Name) + " welcome to the Stones - Paper - Scissors game!")
print("You will be playing against the computer")

while True:
  Player_Input= input("Enter anything out of Stone, Paper OR Scissors.  ")
  if Player_Input.lower() in options:
    comp_choice = random.choice(options)
    print("Computer's choice is " + str(comp_choice))
    game_logic(Player_Input, comp_choice)
    play_again(a)
  else:
   print("Your entry is incorrect")
   print("Game terminted, bye")
   break


  


  



  
