from random import randint
from art import guesser_logo

EASY_TURNS = 10
HARD_TURNS = 5

def difficulty():
    level = input("Easy or hard mode?\n")
    if level == "easy":
        return EASY_TURNS
    elif level == "hard":
        return HARD_TURNS
    
def check_answer(guess, answer, turns):
    """checks answer against guess, returns number of turns remaining"""
    if int(guess) > answer:
        print("Too high!")
        return turns - 1
    elif int(guess) < answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You win! The number was {answer}")

def game():
    answer = randint(1, 100)
    print(guesser_logo)
    print("Guess the number between 1 and 100!\n")
    turns = difficulty()
    guess = 0
    while int(guess) != answer:
        guess = input(f"Make a guess! You have {turns} tries remaining.\n") 
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"Out of turns. The number was: {answer}")

game()