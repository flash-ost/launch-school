from random import choice
from os import system

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
VALID_ANSWERS = ['n', 'no', 'y', 'yes']

# Greet user and explain rules
def greet_user():
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
    prompt('The game is best of 5, ties don\'t count. Good luck!')
    prompt('------------------------------------------------')

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

def host_round():
    global round_count
    prompt(f'Round {round_count}')
    round_count += 1
    user_choice = prompt_input()
    system('clear')
    computer_choice = choice(VALID_CHOICES)
    round_winner = determine_winner(user_choice, computer_choice)
    display_round_result(user_choice, computer_choice, round_winner)

def determine_winner(user, computer):
    if user == computer:
        return False
    elif ((user == 'rock' and computer in ['lizard', 'scissors'])
        or (user == 'paper' and computer in ['rock', 'spock'])
        or (user == 'scissors' and computer in ['paper', 'lizard'])
        or (user == 'lizard' and computer in ['spock', 'paper'])
        or (user == 'spock' and computer in ['scissors', 'rock'])):
        scoreboard['user'] += 1
        return 'user'
    else:
        scoreboard['computer'] += 1
        return 'computer'

# Display round result
def display_round_result(user_choice, computer_choice, winner):
    prompt(f'You chose {user_choice}, computer chose {computer_choice}')
    match winner:
        case 'user':
            prompt('You win!')
        case 'computer':
            prompt('Computer wins!')
        case _:
            prompt('It\'s a tie!')
    prompt(f"""USER [{scoreboard['user']}] : [{scoreboard['computer']}] COMPUTER""")
    prompt('------------------------------------------------')

# Display game result
def display_game_result():
    if scoreboard['user'] == 3:
        prompt(f'You won a game after {round_count} rounds with score {scoreboard['user']}:{scoreboard['computer']}. Congratulations! Did Sheldon train you?')
    else:
        prompt(f'Computer won a game after {round_count} rounds with score {scoreboard['computer']}:{scoreboard['user']}. Better luck next time!')

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

greet_user()
while True:
    round_count = 1
    scoreboard = {'user': 0, 'computer': 0}
    while scoreboard['user'] < 3 and scoreboard['computer'] < 3:
        host_round()
    display_game_result()    
    
    if not another_game():
        break
    system('clear')