
from time import sleep
import random
import re

#Step 1: Read stories from the file
with open("story.txt","r") as file:
    lines = file.readlines()
    stories = [line.strip() for line in lines if line.strip()]

#Step 2: Randomly select a story
story = random.choice(stories) 

#Step 3: Print the selected story
print("Here's a random story for you:\n")

print("Welcome to the Mad Libs Game!")
sleep(3)
print("Please answer the following questions:\n")

name = input("Enter a person's name: ")
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb_past = input("Enter a verb (past tense): ")
adverb = input("Enter an adverb (ends in -ly): ")
adjective2 = input("Enter another adjective: ")
plural_noun = input("Enter a plural noun: ")
exclamation = input("Enter an exclamation (e.g., Wow!): ")
verb_present = input("Enter a verb (present tense): ")
place = input("Enter a place: ")


print("\nHere's your Mad Libs story!\n")
print(f"One sunny morning, {name} woke up feeling especially {adjective1}.")
print(f"He looked out the window and saw a giant {noun1} in the yard!")
print(f"Without thinking, he {verb_past} out the door {adverb} to greet it.")
print(f"The {noun1} handed him a {adjective2} map that pointed to a land filled with sparkling {plural_noun}.")
print(f'"{exclamation}" {name} exclaimed. "This is amazing!"')
print(f"He started {verb_present} all the way to {place}, where the adventure truly began.")

