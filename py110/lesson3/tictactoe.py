from os import system
from random import choice

COMPUTER_MARKER = 'O'
HUMAN_MARKER = 'X'
INITIAL_MARKER = ' '

FIRST_TO_MOVE = 'Choose' # 'Player' 'Computer'
SQUARE_NUMBERS = '123456789'
TOO_MANY_GAMES = 11
VALID_ANSWERS = ['no', 'n', 'yes', 'y']
VALID_DIFFICULTY = ['1', '2', '3', '4']
VALID_FIRST_PLAYER = ['1', '2']
WINNING_LINES = ['123', '456', '789', # rows
                 '147', '258', '369', # columns
                 '159', '357']        # diagonals
WINS_LIMIT = 3

def announce_recent_moves(moves):
    for player in moves:
        if moves[player]:
            prompt(f'{player} chose square {moves[player]}.')

# Ask if user wants to play another match
def another_match():
    print()
    prompt('Fancy another match? Y/N')
    answer = input().strip().lower()
    while answer not in VALID_ANSWERS:
        prompt('Please enter Y for "yes" or N for "no"')
        answer = input().strip().lower()

    return answer in VALID_ANSWERS[2:]

# Check if board is full
def board_full(board):
    return not determine_empty_squares(board)

# Let user change AI difficulty
def change_difficulty():
    print()
    prompt('Tough, right? How about lowering the difficulty? Y/N')
    answer = input().strip()
    while answer not in VALID_ANSWERS:
        prompt('Please type Y for "yes" or N for "no"')
        answer = input().strip().lower()
    return answer in VALID_ANSWERS[2:]

# Let user choose ai difficulty
def choose_difficulty():
    print()
    prompt('***CHOOSE DIFFICULTY LEVEL***')
    prompt('Easy: computer will be very lenient (enter 1)')
    prompt('Medium: computer will try to stop you from winning (enter 2)')
    prompt('Hard: computer will play aggresively (enter 3)')
    prompt('Impossible: you will beg for a tie (enter 4)')

    difficulty = input().strip()
    while difficulty not in VALID_DIFFICULTY:
        prompt('No such difficulty. Enter one of the following numbers:')
        prompt('1 for easy')
        prompt('2 for medium')
        prompt('3 for hard')
        prompt('4 for impossible')
        difficulty = input().strip()
    return difficulty

# Let user/computer choose square
def choose_square(player, board, ai_difficulty):
    if player == 'Player':
        return player_chooses_square(board)
    return computer_chooses_square(board, ai_difficulty)

# Let computer choose square according to difficulty setting
def computer_chooses_square(board, ai_difficulty):
    if board_full(board):
        return None

    match ai_difficulty:
        case '1':
            square = computer_easy(board)
        case '2':
            square = computer_medium(board)
        case '3':
            square = computer_hard(board)
        case '4':
            square = computer_impossible(board)

    board[square] = COMPUTER_MARKER
    return square

# Choose random empty square
def computer_easy(board):
    empty_squares = determine_empty_squares(board)
    return choice(empty_squares)

# Offense: try to win first. If no winning move, try not to let player win
def computer_hard(board):
    square = None
    markers = [COMPUTER_MARKER, HUMAN_MARKER]
    for marker in markers:
        for line in WINNING_LINES:
            markers_in_line = [board[square] for square in line]
            if markers_in_line.count(marker) == 2:
                try:
                    square = line[markers_in_line.index(' ')]
                except ValueError:
                    continue

    # Choose square 5 if it's available, else random square
    if not square:
        empty_squares = determine_empty_squares(board)
        square = '5' if '5' in empty_squares else choice(empty_squares)
    return square

# Choose best square utilizing minimax algorithm
def computer_impossible(board):
    best_score = -float('inf')
    best_square = None
    for square in determine_empty_squares(board):
        board[square] = COMPUTER_MARKER
        score = minimax(board, False)
        board[square] = INITIAL_MARKER
        if score > best_score:
            best_score = score
            best_square = square
    return best_square

# Defense: handle threat of player winning in next move
def computer_medium(board):
    square = None
    for line in WINNING_LINES:
        markers_in_line = [board[square] for square in line]
        if markers_in_line.count(HUMAN_MARKER) == 2:
            try:
                square = line[markers_in_line.index(' ')]
            except ValueError:
                continue

    # Choose random square if no immediate threat
    if not square:
        empty_squares = determine_empty_squares(board)
        square = choice(empty_squares)
    return square

# Return a list of empty squares
def determine_empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

# Display current state of the board
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

# Display game summary
def display_summary(scoreboard):
    print()
    prompt('***CORRENT SCORE***')
    prompt(f'PLAYER {scoreboard['Player']} : '
           f'{scoreboard['Computer']} COMPUTER')

def explain_basics():
    print()
    prompt('Your marker is X, computer\'s marker is O.')
    prompt('Match is played to 3 wins. Good luck!')

def greet_match_winner(scoreboard):
    if scoreboard['Player'] == 3:
        prompt('You\'re a natural! Congratulations on winning the match!')
    else:
        prompt('We trained him well, huh? Better luck next time!')

def greet_player():
    prompt('Let\'s play Tic Tac Toe!')

def host_game(scoreboard, game_number, ai_difficulty):
    # Set who moves first
    if FIRST_TO_MOVE == 'Choose':
        current_player = who_moves_first()
    else:
        current_player = FIRST_TO_MOVE

    # Game preparation
    ready(game_number)
    board = initialize_board()
    recent_squares = {'Player': None, 'Computer': None}

    # Game loop
    while True:
        if current_player == 'Player':
            display_board(board)
            announce_recent_moves(recent_squares)
        recent_squares[current_player] = choose_square(current_player,
                                                       board, ai_difficulty)
        if winner(board) or board_full(board):
            break

        # Alternate player
        current_player = 'Computer' if current_player == 'Player' else 'Player'

    # After game ends
    display_board(board)
    announce_recent_moves(recent_squares)
    record_result(board, scoreboard)
    display_summary(scoreboard)

def host_match():
    difficulty = choose_difficulty()
    explain_basics()
    game_count = 1
    scoreboard = {'Player': 0, 'Computer': 0}
    while (scoreboard['Player'] < WINS_LIMIT
           and scoreboard['Computer'] < WINS_LIMIT):
        # Propose to lower difficulty after lots of ties on impossible
        if game_count == TOO_MANY_GAMES and difficulty == '4':
            if change_difficulty():
                prompt('Sure, let\'s start anew!')
                host_match()
            else:
                prompt('No problem, you seem to like it. =)')

        host_game(scoreboard, game_count, difficulty)
        game_count += 1
    greet_match_winner(scoreboard)

def initialize_board():
    return {key: INITIAL_MARKER for key in SQUARE_NUMBERS}

# Check whether chosen square is valid
def is_valid_square(square_num, empties):
    return square_num in empties

# Proper formatting for available squares
def join_or(sequence, delimiter=', ', join_word='or'):
    match len(sequence):
        case 0:
            return ''
        case 1:
            return sequence[0]
        case 2:
            return f'{sequence[0]} {join_word} {sequence[1]}'
        case _:
            return (f'{delimiter.join(sequence[:-1])}'
                    f'{delimiter}{join_word} {sequence[-1]}')

# Minimax algorithm for impossible difficulty
def minimax(board, maximizing):
    # Base case 1: we have a winner
    won = winner(board)
    if won:
        return 1 if won == 'Computer' else -1
    # Base case 2: board is full
    if board_full(board):
        return 0

    # Recursive case
    if maximizing:
        best_score = -float('inf')
        for square in determine_empty_squares(board):
            board[square] = COMPUTER_MARKER
            score = minimax(board, False)
            board[square] = INITIAL_MARKER
            best_score = max(score, best_score)
    else:
        best_score = float('inf')
        for square in determine_empty_squares(board):
            board[square] = HUMAN_MARKER
            score = minimax(board, True)
            board[square] = INITIAL_MARKER
            best_score = min(score, best_score)
    return best_score

# Let player choose a square
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
    return square

# Main program
def play_tictactoe():
    while True:
        system('clear')
        greet_player()
        host_match()
        if not another_match():
            prompt('Thank you for playing!')
            break

# Format messages
def prompt(message):
    print(f'==> {message}')

# Announce game number and ensure player is ready
def ready(game_number):
    print()
    prompt(f'Game {game_number} begins!')
    prompt('Press ENTER when ready')
    input()

# Update scoreboard after game
def record_result(board, scoreboard):
    result = winner(board)
    if result:
        prompt(f'{result} won!')
        scoreboard[result] += 1
    else:
        prompt('It\'s a tie!')

# Let user choose who makes first move
def who_moves_first():
    print()
    prompt('***CHOOSE WHO MOVES FIRST***')
    prompt('You: enter 1')
    prompt('Computer: enter 2')
    move_order = input().strip()
    while move_order not in VALID_FIRST_PLAYER:
        prompt('Please enter 1 if you want to move first, 2 if second.')
        move_order = input().strip()
    return 'Player' if move_order == '1' else 'Computer'

# Determine if there is a winner
def winner(board):
    for line in WINNING_LINES:
        line_markers = set([board[line[0]], board[line[1]], board[line[2]]])
        if line_markers == set(HUMAN_MARKER):
            return 'Player'
        if line_markers == set(COMPUTER_MARKER):
            return 'Computer'
    return None

play_tictactoe()