from supportfiles._hl_data import data
from os import system
import random
from supportfiles.art import hl_logo, hl_vs

def get_contestant():
    contestant = random.choice(data)
    data.remove(contestant)
    return contestant

def contestant_string(dict):
    return(f"{dict['name']}, a {dict['description']} from {dict['country']}")

def player_win():
    global playerscore
    playerscore += 1
    cont = input(f"You got it! Your score is {playerscore}. Keep playing? Y or N: ")
    if cont == "n":
        global is_playing
        is_playing = False
    else:
        global replay
        replay = True
        system("cls")

def player_lose():
    print(f"Wrong! Game over. Your score was {playerscore}.")
    global is_playing
    is_playing = False

playerscore = 0
is_playing = True
replay = False

def maingame():
    print(hl_logo)
    if replay == True:
        contestant_a = nextround
    else:
        contestant_a = get_contestant()
    print(f"Compare A: {contestant_string(contestant_a)}")
    print(hl_vs)
    contestant_b = get_contestant()
    print(f"To B: {contestant_string(contestant_b)}")
    guess = input("Which do you think has more Instagram followers? Choose A or B: ")
    if guess == "a":
        if contestant_a['follower_count'] > contestant_b['follower_count']:
            player_win()
            return contestant_a
        else:
            player_lose()
    else:
        if contestant_b['follower_count'] > contestant_a['follower_count']:
            player_win()
            return contestant_b
        else:
            player_lose()

while is_playing == True:
    nextround = maingame()