from os import system
from random import choice

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
SQUARE_NUMBERS = '123456789'
VALID_ANSWERS = ['no', 'n', 'yes', 'y']
WINNING_LINES = ['123', '456', '789', # rows
                 '147', '258', '369', # columns
                 '159', '357']        # diagonals

def computer_chooses_square(board):
    if board_full(board):
        return
    empty_squares = determine_empty_squares(board)
    computer_square = choice(empty_squares)
    board[computer_square] = COMPUTER_MARKER

def determine_empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def display_board(board):
    system('clear')
    print()
    print('     |     |')
    print(f'  {board['1']}  |  {board['2']}  |  {board['3']}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board['4']}  |  {board['5']}  |  {board['6']}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board['7']}  |  {board['8']}  |  {board['9']}')
    print('     |     |')
    print()

def initialize_board():
    return {key: INITIAL_MARKER for key in SQUARE_NUMBERS}

def join_or(sequence, delimiter=', ', join_word='or'):
    match len(sequence):
        case 0:
            return ''
        case 1:
            return sequence[0]
        case 2:
            return f'{sequence[0]} {join_word} {sequence[1]}'
        case _:
            return f'{delimiter.join(sequence[:-1])}{delimiter}{join_word} {sequence[-1]}'

def prompt(message):
    print(f'==> {message}')

def player_chooses_square(board):
    # Determine what squares are empty
    empty_squares = determine_empty_squares(board)
    while True:
        prompt(f'Choose a square ({join_or(empty_squares)}):')
        square = input().strip()
        if is_valid_square(square, empty_squares):
            break
        prompt('Sorry, that\'s not a valid square.')
    board[square] = HUMAN_MARKER

def is_valid_square(square_num, empties):
    return square_num in empties

def board_full(board):
    return not determine_empty_squares(board)

def winner(board):
    for line in WINNING_LINES:
        line_markers = set([board[line[0]], board[line[1]], board[line[2]]])
        if line_markers == set(HUMAN_MARKER):
            return 'Player'
        elif line_markers == set(COMPUTER_MARKER):
            return 'Computer'
    return None  

def host_game():
    greet_player()
    board = initialize_board()

    while True:
        display_board(board)

        player_chooses_square(board)
        if winner(board) or board_full(board):
            break

        computer_chooses_square(board)
        if winner(board) or board_full(board):
            break

    display_board(board) 
    display_result(board)    

def display_result(board):
    result = winner(board)
    if result:
        prompt(f'{result} won!')
    else:
        prompt('It\'s a tie!')

def another_game():
    prompt('Fancy another game? Y/N')
    answer = input().strip().lower()
    while answer not in VALID_ANSWERS:
        prompt('What-what? Type Y for "yes" or N for "no"')
        answer = input().strip().lower()

    return answer in VALID_ANSWERS[2:]

def greet_player():
    prompt('Let\'s play Tic Tac Toe!')
    prompt('Your marker is "X", computer\'s marker is O. Good luck!')
    prompt('Ready? Y/N')
    
    answer = input().strip().lower()
    while answer not in VALID_ANSWERS[2:]:
        answer = input().strip().lower()

while True:
    host_game()
    if not another_game():
        prompt('Thank you for playing!')
        break
