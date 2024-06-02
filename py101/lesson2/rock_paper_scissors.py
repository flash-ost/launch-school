from random import choice
from os import system

VALID_CHOICES = ['rock', 'paper', 'scissors']
VALID_ANSWERS = ['n', 'no', 'y', 'yes']

# Print a formatted message
def prompt(message):
    print(f"==> {message}")

# Ask user to make a choice
def prompt_input():
    prompt('Choose one: ' + ', '.join(VALID_CHOICES))
    choice = input()
    while choice not in VALID_CHOICES:
        prompt('That\'s not a valid choice')
        choice = input()
    return choice

# Compare choices and display result
def display_result(user_choice, computer_choice):
    prompt(f'You chose {user_choice}, computer chose {computer_choice}')
    if user_choice == computer_choice:
        prompt('It\'s a tie!')
    elif ((user_choice == 'rock' and computer_choice == 'scissors')
        or (user_choice == 'paper' and computer_choice == 'rock')
        or (user_choice == 'scissors' and computer_choice == 'paper')):
        prompt('You win!')
    else:
        prompt('Computer wins!')

def another_round():
    prompt('Would you like to play another round? Y/N')
    answer = input()
    while True:
        if answer.lower() not in VALID_ANSWERS:
            prompt('Please enter Y for yes or N for no.')
            answer = input()
        else:
            break
    return answer.lower() in ['y', 'yes']       

while True:
    user_choice = prompt_input()
    computer_choice = choice(VALID_CHOICES)
    display_result(user_choice, computer_choice)
    
    if not another_round():
        break
    system('clear')