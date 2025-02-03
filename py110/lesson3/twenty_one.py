from random import shuffle
from os import system

HIT_CAP = 17
MAX_HAND = 21
MAX_WINS = 3
SUITS = '♠♥♦♣'
VALID_ANSWERS = ('n', 'no', 'y', 'yes')
VALID_MOVES = ('h', 'hit', 's', 'stay')
VALUES = { '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
           '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11, }

# Format message
def prompt(message):
    print(f'==> {message}')

def greet_player():
    system('clear')
    prompt('Let\'s play Twenty-One!')
    prompt('Game format is best of 5. Good luck!')

def ready(round_number):
    print()
    prompt(f'Round {round_number} begins!')
    prompt('Press ENTER when ready')
    input()

def generate_deck():
    deck = [suit + value for suit in SUITS for value in VALUES]
    shuffle(deck)
    return deck

# Check if player busted
def busted(total_value):
    return total_value > MAX_HAND

def display_cards(hands, final_display):
    system('clear')
    for player in hands:
        rows = ['', '', '', '', '']
        print(f'{player.upper()}\'S HAND')
        hand = hands[player]

        # If not final display, second dealer's card should be face down
        if player == 'Dealer' and not final_display:
            hand = [hands[player][0], '??']
        for card in hand:
            suit = card[0]
            value_top = card[1:] if card[1:] == '10' else f'{card[1:]} '
            value_bottom = card[1:] if card[1:] == '10' else f' {card[1:]}'
            rows[0] += '+-----+  '
            rows[1] += f'|{value_top}   |  '
            rows[2] += f'|  {suit}  |  '
            rows[3] += f'|   {value_bottom}|  '
            rows[4] += '+-----+  '

        for row in rows:
            print(row)

# Calculate total value of player's cards
def total(hands, player):
    values = [card[1:] for card in hands[player]]
    value_sum = 0

    for value in values:
        value_sum += VALUES[value]

    aces = values.count('A')
    while value_sum > MAX_HAND and aces:
        value_sum -= 10
        aces -= 1

    return value_sum

def player_turn(hands, deck):
    while True:
        total_value = total(hands, 'Player')
        if busted(total_value):
            return True, total_value

        display_cards(hands, False)
        prompt(f'Your hand value is {total_value}')
        prompt('Do you want to hit or stay? H/S')
        move = input().strip().lower()
        while move not in VALID_MOVES:
            prompt('Please enter H for hit or S for stay:')
            move = input().strip().lower()

        if move in VALID_MOVES[:2]:
            hands['Player'].append(deck.pop())
        else:
            return False, total_value

def dealer_turn(hands, deck):
    while True:
        total_value = total(hands, 'Dealer')
        if busted(total_value):
            return True, total_value
        if total_value >= HIT_CAP:
            return False, total_value
        hands['Dealer'].append(deck.pop())

def announce_hand_values(player_total, dealer_total):
    prompt(f'Your hand value is {player_total}')
    prompt(f'Dealer\'s hand value is {dealer_total}')

def determine_winner(player_busted, player_total, dealer_busted, dealer_total):
    if player_busted:
        prompt('You busted, dealer wins!')
        return 'Dealer'
    if dealer_busted:
        prompt('Dealer busted, you win!')
        return 'Player'
    if player_total > dealer_total:
        prompt('Your hand is higher, you win!')
        return 'Player'
    if player_total < dealer_total:
        prompt('Dealer\'s hand is higher, you lose!')
        return 'Dealer'
    prompt('It\'s a tie!')
    return None

def update_scoreboard(winner, scoreboard):
    if winner:
        scoreboard[winner] += 1

def display_scores(scoreboard):
    print()
    prompt('***CURRENT SCORE***')
    prompt(f'PLAYER {scoreboard['Player']} : '
           f'{scoreboard['Dealer']} DEALER')

def host_round():
    round_count = 1
    scoreboard = {'Player': 0, 'Dealer': 0}
    while True:
        ready(round_count)
        deck = generate_deck()
        hands = { 'Dealer': [deck.pop(), deck.pop()],
                  'Player': [deck.pop(), deck.pop()] }

        # Player and dealer play hands
        player_busted, player_total = player_turn(hands, deck)
        if player_busted:
            dealer_busted, dealer_total = False, total(hands, 'Dealer')
        else:
            dealer_busted, dealer_total = dealer_turn(hands, deck)

        # Final reveal
        display_cards(hands, True)
        announce_hand_values(player_total, dealer_total)

        winner = determine_winner(player_busted, player_total,
                                  dealer_busted, dealer_total)
        update_scoreboard(winner, scoreboard)
        display_scores(scoreboard)
        round_count += 1
        if MAX_WINS in {scoreboard['Dealer'], scoreboard['Player']}:
            announce_game_winner(scoreboard)
            break

def announce_game_winner(scoreboard):
    if scoreboard['Player'] == MAX_WINS:
        prompt('You won the game, congratulations!')
    else:
        prompt('Dealer beat you! Better luck next time.')

# Ask if user wants to play another game
def another_game():
    print()
    prompt('Fancy another game? Y/N')
    answer = input().strip().lower()
    while answer not in VALID_ANSWERS:
        prompt('Please enter Y for "yes" or N for "no"')
        answer = input().strip().lower()
    return answer in VALID_ANSWERS[2:]

# Main program
def play_twenty_one():
    greet_player()
    while True:
        host_round()
        if not another_game():
            prompt('Thank you for playing!')
            break
        system('clear')

play_twenty_one()        