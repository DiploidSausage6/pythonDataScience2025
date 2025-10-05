# a python program to return a random joke from a list of jokes

import random

jokes = [
    "Why did the student eat his homework? Because the teacher said it was a piece of cake!",
    "Why can't you trust atoms? Because they make up everything!",
    "What did one pencil say to the other pencil? You're looking sharp!",
    "Why did the computer go to the doctor? It had a virus!",
    "What's a math teacher's favorite place in New York? Times Square!",
    "Why was the math book sad? Because it had too many problems.",
    "What did the science book say to the history book? You're too old school!",
    "Why did the music teacher need a ladder? To reach the high notes!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What's a ghost's favorite subject? Spelling!"
]

def jokeFetcher(): 
    print(jokes[random.randint(0,len(jokes) -1)]) #
