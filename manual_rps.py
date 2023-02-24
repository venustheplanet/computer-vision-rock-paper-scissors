import random

def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def get_user_choice():
    return input('Please choose Rock, Paper, or Scissors: ')

def get_winner(computer_choice, user_choice):
    if (computer_choice == 'Rock' and user_choice == 'Scissors') or (computer_choice == 'Paper' and user_choice == 'Rock') or (computer_choice == 'Scissors' and user_choice == 'paper'):
        print("You lost")
    elif computer_choice == user_choice:
        print("It is a tie!")
    else:
        print("You won!")

def play():
    computer_choice = get_computer_choice()
    # print('computer_choice', computer_choice)
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)

play()