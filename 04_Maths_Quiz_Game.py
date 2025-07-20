import random
from time import sleep
import time
#Game Rules
print("===== Welcome to the : MATHS QUIZ GAME =====")
sleep(3)
print("Rules:")
sleep(1)
print("1) You will provide a random mathematical expression and you need to guess the calculation of it.")
print("2) You will be given 5 attempts and all these attempts will be timed")
print("3) You need answer correctly.")
print("Let's begin!\n")


#Generate Expressions 
def generate_question():
  left = random.choice(OPERANDS)
  right = random.choice(OPERANDS)
  operator = random.choice(OPERATORS)
  expr = str(left) + " " + str(operator) + " " + str(right)
  print(expr)
  return expr

# Take input from the user
# Check if the answer is correct


i = 0
total_correct = 0
total_incorrect = 0
OPERATORS = ['+', '-', '*']
OPERANDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
TOTAL_PROBLEMS = 5
start_time = time.time()


user_choice = input("Enter Y to START the GAME. Else the game will TERMINATE.   ")
if user_choice == 'y' or user_choice =='Y':
   while i < TOTAL_PROBLEMS:
      exp = generate_question()
      answer = input("Enter your answer: ")
      if eval(exp) == int(answer):  # Changed to float for division cases
         print("Correct!")
         total_correct += 1
      else:
         print("Incorrect!")
         total_incorrect += 1
      i += 1
      print("--------------")
else:
   print("Game Terminated. Bye!")
   quit()

end_time= time.time()
total_time = round(end_time-start_time,2)
print("Nice Work! 5 Questions Done")
print("Total correct answers:", total_correct)
print("Total time taken:", str(total_time), "seconds")
