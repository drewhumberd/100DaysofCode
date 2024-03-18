import random
import os

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

cards_dict = {
    "A": 11,
    "J": 10,
    "Q": 10,
    "K": 10   
    }

def deal_card():
    '''Deals a random card.'''
    return random.choice(cards)

game_active = True

while game_active == True:
    # creates hands as empty lists
    user_cards = []
    computer_cards = []

    # deals two cards to each player
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def calculate_score(cards):
        '''Calculates score for called player. If hand is blackjack (Ace + 10 or Face Card), set value to 0. Ace is worth 11 unless score would be > 21.'''
        hand_value = []
        for x in cards:
            if x == "A" or x == "J" or x == "Q" or x == "K":
                hand_value.append(cards_dict[x])
            else:
                hand_value.append(x)
        if len(cards) == 2 and sum(hand_value) == 21:
            return 0
        else:
            if 11 in hand_value and sum(hand_value) > 21:
                hand_value.remove(11)
                hand_value.append(1)
            return sum(hand_value)
        
    player_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards) # check scores
    stand = False
    while stand == False: # allow player to draw additional cards
        hit = input(f"""
                    Your hand is {user_cards}
                    Do you want to draw another card?
                    """)
        if hit == "no" or hit == "n":
            stand = True
        else:
            user_cards.append(deal_card())
            player_score = calculate_score(user_cards)
            
    computer_score = calculate_score(computer_cards)

    while computer_score != 0 and computer_score < 17: # computer always hits on hands 16 or lower, stands otherwise
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    def compare_score():
        if computer_score == 0:
            print("The computer has a blackjack! You lose")
        elif player_score == 0:
            print("Blackjack! You win")
        elif player_score > 21 and computer_score > 21:
            print("You both bust! Draw")
        elif player_score > 21:
            print("Bust! You lose")
        elif computer_score > 21:
            print("Computer busts! You win")
        elif computer_score == player_score:
            print("It's a draw")
        elif computer_score > player_score:
            print("You lose!")
        else:
            print("You win!")
    print(f"Your hand: {user_cards} = {player_score}")
    print(f"Computer's hand: {computer_cards} = {computer_score}")
    compare_score()
    replay = input("Play again?")
    if replay == "yes" or replay == "y":
        os.system("cls")
    else:
        game_active = False