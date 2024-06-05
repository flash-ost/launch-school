from random import choice
from os import system

VALID_CHOICES = {
    'r': 'rock',
    'p': 'paper',
    'sc': 'scissors',
    'l': 'lizard',
    'sp': 'spock',
}
VALID_ANSWERS = ['n', 'no', 'y', 'yes']
WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['paper',    'spock'],
    'spock':    ['rock',     'scissors'],
}
WINS_LIMIT = 3

# Greet user and explain rules
def greet_user():
    system('clear')
    prompt('Welcome to game Rock, Paper, Scissors, Lizard, Spock!')
    prompt("""The rules are (not so) simple:
           Scissors cut Paper
           Paper covers Rock
           Rock crushes Lizard
           Lizard poisons Spock
           Spock smashes Scissors
           Scissors decapitate Lizard
           Lizard eats Paper
           Paper disproves Spock
           Spock vaporizes Rock
           Rock crushes Scissors""")
    prompt('The game is played to 3 wins, ties don\'t count. Good luck!')
    prompt('----------------------------------------------------------')

# Print a formatted message
def prompt(message):
    print(f"==> {message}")

# Ask user to make a choice
def prompt_input():
    prompt('Choose one: ' + ', '.join(VALID_CHOICES.values()))
    prompt('You can also type abbreviated names: ' +
           ', '.join(VALID_CHOICES.keys()))
    user_choice = input().lower()

    # Ensure input is valid
    while user_choice not in VALID_CHOICES \
    and user_choice not in VALID_CHOICES.values():
        prompt('That\'s not a valid choice')
        user_choice = input()

    # Ensure full name is stored
    if len(user_choice) <= 2:
        user_choice = VALID_CHOICES[user_choice]
    return user_choice

# Host a round
def host_round():
    prompt(f'Round {round_count}')

    # Gather input from user and computer
    user_choice = prompt_input()
    computer_choice = choice(tuple(VALID_CHOICES.values()))

    # Display winner and score
    system('clear')
    round_winner = determine_winner(user_choice, computer_choice)
    if round_winner:
        scoreboard[round_winner] += 1
    display_round_result(user_choice, computer_choice, round_winner)

# Determine winner (or tie)
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return False
    return 'user' if computer_choice in WINNING_COMBOS[user_choice] \
        else 'computer'

# Display round result
def display_round_result(user_choice, computer_choice, winner):
    prompt(f'Round {round_count} results')
    prompt(f'You chose {user_choice}, computer chose {computer_choice}')
    match winner:
        case 'user':
            prompt('You win!')
        case 'computer':
            prompt('Computer wins!')
        case False:
            prompt('It\'s a tie!')
    prompt(f'USER [{scoreboard['user']}] : '
           f'[{scoreboard['computer']}] COMPUTER')
    prompt('------------------------------------------------')

# Display game result
def display_game_result():
    if scoreboard['user'] == 3:
        prompt(f'You won a game after {round_count} rounds with score '
               f'{scoreboard['user']}:{scoreboard['computer']}. '
               'Congratulations! Did Sheldon train you?')
    else:
        prompt(f'Computer won a game after {round_count} rounds with score '
               f'{scoreboard['computer']}:{scoreboard['user']}. '
               'Better luck next time!')

# Ask user for another game
def another_game():
    prompt('Would you like to play another game? Y/N')
    answer = input()
    while True:
        if answer.lower() not in VALID_ANSWERS:
            prompt('Please enter Y for yes or N for no.')
            answer = input()
        else:
            break
    return answer.lower() in ['y', 'yes']

# Main program
greet_user()
while True:
    round_count = 0
    scoreboard = {'user': 0, 'computer': 0}
    while scoreboard['user'] < WINS_LIMIT \
    and scoreboard['computer'] < WINS_LIMIT:
        round_count += 1
        host_round()
    display_game_result()

    if not another_game():
        break
    system('clear')