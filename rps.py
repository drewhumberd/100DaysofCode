rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
player_choice = input("Choose Rock, Paper, or Scissors.\n")
if player_choice == "rock":
    print("Your choice is Rock" + rock)
    playoutcome = 1
elif player_choice == "paper":
    print("Your choice is Paper" + paper)
    playoutcome = 2
else:
    print("Your choice is Scissors" + scissors)
    playoutcome = 3
randoutcome = random.randint(1, 3)
# 1 = rock
# 2 = paper
# 3 = scissors
if randoutcome == 1:
    print("Computer's choice is Rock" + rock)
elif randoutcome == 2:
    print("Computer's choice is Paper" + paper)
else:
    print("Computer's choice is Scissors" + scissors)
rock_vs_paper = "Paper wraps Rock. "
rock_vs_scissors = "Rock crushes Scissors. "
scissors_vs_paper = "Scissors cut Paper. "
rock_vs_rock = "Rock and Rock tie."
paper_vs_paper = "Paper and Paper tie."
scissors_vs_scissors = "Scissors and Scissors tie."
lose = "You lose!"
win = "You win!"
if player_choice == "rock":
    if randoutcome == 1:
        print(rock_vs_rock)
    elif randoutcome == 2:
        print(rock_vs_paper + lose)
    else:
        print(rock_vs_scissors + win)
elif player_choice == "paper":
    if randoutcome == 1:
        print(rock_vs_paper + win)
    elif randoutcome == 2:
        print(paper_vs_paper)
    else:
        print(scissors_vs_paper + lose)
else:
    if randoutcome == 1:
        print(rock_vs_scissors + lose)
    elif randoutcome == 2:
        print(scissors_vs_paper + win)
    else:
        print(scissors_vs_scissors)