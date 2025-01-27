from random import choice, shuffle
from os import system

HIT_CAP = 17
MAX_HAND = 21
MAX_WINS = 3
SUITS = '♠♥♦♣'
VALID_ANSWERS = ('n', 'no', 'y', 'yes')
VALID_MOVES = ('h', 'hit', 's', 'stay')
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10',
          'J', 'Q', 'K', 'A')



def busted(hands, player):
    return total(hands, player) > MAX_HAND

def dealer_move(hands, deck):
    while True:
        if busted(hands, 'Dealer'):
            return 'Busted'
        elif total(hands, 'Dealer') >= HIT_CAP:
            return 'Stay'
        else:
            hands['Dealer'].append(deck.pop())

def display_cards(hands, final_display):
    system('clear')
    for player in hands:
        rows = ['', '', '', '', '']
        print(f'***{player.upper()}\'S HAND***')
        hand = hands[player]
        if player == 'Dealer' and not final_display:
            hand = [hands[player][0], '??']
        for card in hand:
            suit = card[0]
            value1 = card[1:] if card[1:] == '10' else f'{card[1:]} '
            value2 = card[1:] if card[1:] == '10' else f' {card[1:]}'
            rows[0] += '+-----+  '
            rows[1] += f'|{value1}   |  '
            rows[2] += f'|  {suit}  |  '
            rows[3] += f'|   {value2}|  '
            rows[4] += '+-----+  '

        for row in rows:
            print(row)

def display_summary(scoreboard):
    print()
    prompt('***CURRENT SCORE***')
    prompt(f'PLAYER {scoreboard['Player']} : '
           f'{scoreboard['Dealer']} DEALER')    

def generate_deck():
    deck = [suit + value for suit in SUITS for value in VALUES]
    shuffle(deck)
    return deck

def greet_player():
    system('clear')
    prompt('Let\'s play twenty-one!')
    prompt(f'Whoever wins {MAX_WINS} rounds first wins the game. Good luck!')

def player_move(hands, deck):
    while True:
        display_cards(hands, False)
        prompt(f'Do you want to hit or stay? H/S')
        move = input().strip().lower()
        while move not in VALID_MOVES:
            prompt('Please enter H for hit or S for stay:')
            move = input().strip().lower()

        if move in VALID_MOVES[:2]:
            hands['Player'].append(deck.pop())
            if busted(hands, 'Player'):
                return 'Busted'
        else:
            return 'Stay'

# Format message
def prompt(message):
    print(f'==> {message}')

def ready(round_number):
    print()
    prompt(f'Round {round_number} begins!')
    prompt('Press ENTER when ready')
    input()    

def total(hands, player):
    values = [card[1:] for card in hands[player]]
    value_sum = 0


    for value in values:
        if value == 'A':
            value_sum += 11
        elif value in 'JQK':
            value_sum += 10
        else:
            value_sum += int(value)

    aces = values.count('A')
    while value_sum > MAX_HAND and aces:
        value_sum -= 10
        aces -= 1

    return value_sum    

greet_player()
round_count = 1
scoreboard = {'Player': 0, 'Dealer': 0}
while True:
    deck = generate_deck()
    ready(round_count)
    hands = { 'Dealer': [deck.pop(), deck.pop()],
              'Player': [deck.pop(), deck.pop()] }
    
    player_decision = player_move(hands, deck)
    if player_decision == 'Busted':
        display_cards(hands, False)
        prompt(f'Your hand value is {total(hands, 'Player')}')
        prompt('You busted, dealer wins!')
        scoreboard['Dealer'] += 1
    else:
    
        dealer_decision = dealer_move(hands, deck)

        display_cards(hands, True)
        prompt(f'Your hand value is {total(hands, 'Player')}')
        prompt(f'Dealer\'s hand value is {total(hands, 'Dealer')}')

        if dealer_decision == 'Busted':
            prompt('Dealer busted, you win!')
            scoreboard['Player'] += 1
        else:
            # Player won
            if total(hands, 'Player') > total(hands, 'Dealer'):
                prompt('You hand is higher, you win!')
                scoreboard['Player'] += 1

            # Computer won
            elif total(hands, 'Player') < total(hands, 'Dealer'):
                prompt('Dealer\'s hand is higher, you lose!')
                scoreboard['Dealer'] += 1

            # Tie
            else:    
                prompt('It\'s a tie!')

    display_summary(scoreboard)
    round_count += 1
    if scoreboard['Dealer'] == MAX_WINS or scoreboard['Player'] == MAX_WINS:
        break