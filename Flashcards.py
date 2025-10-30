# this is a program to generate random flashcards 
def getFlashcards(): # function to store the flashcards
    flashcards = [
        ("What is the capital of France?", "Paris"),
        ("What is 7 times 8?", "56"),
        ("What is the largest planet in our solar system?", "Jupiter"),
        ("What is the chemical symbol for gold?", "Au"),
        ("Who wrote 'To Kill a Mockingbird'?", "Harper Lee")
    ]
    return flashcards

import random

def getRandomCard(flashcards): # function to return a random flashcard from the list
  return random.choice(flashcards)

def runFlashcards():
  flashcards = getFlashcards()
  print("Here is a flashcard game!")
  print("type 'quit' to leave")

  while True:
    question, answer = getRandomCard(flashcards) # get a random card
    print(f"\nQuestion: {question}") # prints on a new line the question
    userInput = input("your answer: ") # get user's answer
    
    if userInput.lower() == 'quit': # determines whether the user wants to quit
      print("Thanks for playing!")
      break
    elif userInput.lower() == "i don't know":
        print(f"ha! you need some help? ok, here's the answer: {answer}")
        
    elif userInput.lower() == answer.lower(): # determines whether the user is correct or incorrect and prints the correct answer if incorrect
      print("Correct!")
    else:
      print(f"Incorrect. The correct answer is: {answer}")

runFlashcards() # call the function to start the game
