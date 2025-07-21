import random 
from time import sleep
import os

#Game Rules 

print("Welcome to MADLIBS GAME")
print("You will be asked few words to fill in the story picked randomly from our collections of 5 stories. ")
sleep(2)
print("Let's start")


def select_story(adjective, noun,verb):
   file_path = "story.txt"
   
   if os.path.exists(file_path):
    with open(file_path, 'r') as file:
       content = file.read()
       stories = [story.strip() for story in content.split("=== STORY ===") if story.strip()]
       selected_story = random.choice(stories)
       filled_story = selected_story.format(adjective=adjective, noun=noun, verb=verb)
    print("\n🎉 Here's your MadLibs story:\n")
    print(filled_story)
   else:
     print("Some error reported")

print("🎯 Let's build your story! I just need three words:")
adjective = input("👉 Enter an *adjective* (describing word, like 'funny', 'smelly', 'brght'):")
noun = input("👉 Enter a *noun* (a thing or person, like 'cat', 'robot', 'sandwich'): ")
verb = input("👉 Enter a *verb* (an action, like 'dance', 'explode', 'hide'): ")
print("Wait while we are generating the story")
sleep(2)
select_story(adjective, noun,verb)
