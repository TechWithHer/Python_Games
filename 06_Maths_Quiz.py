import random
import time

OPERATORS = ['+', '-', '*']
OPERANDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
TOTAL_PROBLEMS = 5

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

play = input("Do you want to play? 'y' to start any other button to exit:  ")
#check if they want to play

if play == "y":
  print("--------------")
  print("Welcome to the Math Quiz!")
  start_time=time.time()
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
  end_time=time.time()
  total_time= round(end_time-start_time,2)
  print("Nice Work! 5 Questions Done")
  print("Total correct answers:", total_correct)
  print("Total incorrect answers:", total_incorrect)
  print("Total time taken:", str(total_time), "seconds")
   
else:
    print("Goodbye")
    quit()
  
