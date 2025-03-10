import random
import os

clear = lambda: os.system('cls')

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
    



def paly_game():
    is_game_over = False
    user_cards = []
    computer_cards = []


    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f" Your cards: {user_cards},current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")


        if user_score == 0 or computer_score ==0 or user_score > 21:
            is_game_over = True
        else:
            value = input("Enter 'y' to continue or enter 'n' for exit...")
            if value == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f" Your final hand : {user_cards},final score {computer_cards} ")
    print(compare(user_score,computer_score))



while input("'Do you want to play Blackjack? Type 'y' or 'n' : ") == "y":
    clear()
    paly_game()