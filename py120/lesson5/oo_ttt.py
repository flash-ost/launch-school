from os import system
from random import choice

class Square:
    INITIAL_MARKER = ' '
    HUMAN_MARKER = 'X'
    COMPUTER_MARKER = 'O'

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

    def __str__(self):
        return self.marker

class Board:
    SQUARE_NUMBERS = '123456789'

    def __init__(self):
        self.reset()

    def count_markers(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

    def display(self):
        system('clear')
        print('     |     |')
        print(f'  {self.squares['1']}  |'
              f'  {self.squares['2']}  |'
              f'  {self.squares['3']}')
        print('     |     |')
        print('-----+-----+-----')
        print('     |     |')
        print(f'  {self.squares['4']}  |'
              f'  {self.squares['5']}  |'
              f'  {self.squares['6']}')
        print('     |     |')
        print('-----+-----+-----')
        print('     |     |')
        print(f'  {self.squares['7']}  |'
              f'  {self.squares['8']}  |'
              f'  {self.squares['9']}')
        print('     |     |')
        print()

    def is_full(self):
        return len(self.unused_squares()) == 0

    def is_unused_square(self, key):
        return self.squares[key].is_unused()

    def mark_square(self, key, marker):
        self.squares[key].marker = marker

    def reset(self):
        self.squares = {num: Square() for num in Board.SQUARE_NUMBERS}

    def unused_squares(self):
        return [key for key, square in self.squares.items()
                if square.is_unused()]

class Player:
    def __init__(self, marker):
        self.marker = marker
        self._score = 0

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    TOO_MANY_ROUNDS = 10
    VALID_ANSWERS = ('y', 'yes', 'n', 'no')
    VALID_DIFFICULTY = ('1', '2', '3', '4')
    VALID_FIRST_PLAYER = ('1', '2')
    WIN_LINES = ('123', '456', '789', # rows
                 '147', '258', '369', # columns
                 '159', '357')        # diagonals
    WINS_LIMIT = 3

    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self.difficulty = None
        self.first_player = None
        self.round_count = 0

    def play(self):
        self.display_welcome_message()
        while True:
            self.host_match()
            if not self.play_again():
                break
            system('clear')
            print("Let's play again!")

        self.display_goodbye_message()

    def host_match(self):
        self.prepare_match()
        while True:
            self.host_round()
            if TTTGame.WINS_LIMIT in (self.human.score, self.computer.score):
                break
            self.round_count += 1
            if self.round_count == TTTGame.TOO_MANY_ROUNDS:
                if self.change_difficulty():
                    system('clear')
                    print('Sure, let\'s start anew!')
                    self.prepare_match()
                    continue
                print()
                print('No problem, you seem to like it. =)')
            input('Press ENTER when ready for the next round: ')
            system('clear')
            self.board.reset()
        self.display_match_results()

    def prepare_match(self):
        self.board.reset()
        self.reset_scores()
        self.round_count = 0
        self.set_difficulty()
        self.choose_who_moves_first()

    def reset_scores(self):
        self.human.score = 0
        self.computer.score = 0

    def set_difficulty(self):
        print()
        print('CHOOSE DIFFICULTY LEVEL')
        print('Easy: computer will be very lenient (enter 1)')
        print('Medium: computer will try to stop you from winning (enter 2)')
        print('Hard: computer will play aggresively (enter 3)')
        print('Impossible: you will beg for a tie (enter 4)')

        while True:
            difficulty = input().strip()
            if difficulty in TTTGame.VALID_DIFFICULTY:
                break
            print('No such difficulty. Enter one of the following numbers:')
            print('1 for easy')
            print('2 for medium')
            print('3 for hard')
            print('4 for impossible')
        self.difficulty = difficulty
        system('clear')

    def choose_who_moves_first(self):
        print()
        print('CHOOSE WHO MOVES FIRST (order swaps every round)')
        print('You: enter 1')
        print('Computer: enter 2')

        while True:
            first = input().strip()
            if first in TTTGame.VALID_FIRST_PLAYER:
                break
            print('Please enter 1 if you want to move first, 2 if second.')

        self.first_player = self.human if first == '1' else self.computer
        system('clear')

    def host_round(self):
        current_player = self.first_player
        while True:
            if current_player == self.human:
                self.board.display()
            self.player_moves(current_player)
            current_player = self.toggle_player(current_player)
            if self.is_game_over():
                self.board.display()
                break
        self.update_score()
        self.display_round_results()
        self.first_player = self.toggle_player(self.first_player)

    def player_moves(self, player):
        if player == self.human:
            self.human_moves()
        else:
            self.computer_moves()

    def human_moves(self):
        valid_choices = self.board.unused_squares()
        choices_str = self._join_or(valid_choices)
        prompt = f'Choose a square ({choices_str}): '
        while True:
            move = input(prompt).strip()
            if move in valid_choices:
                break

            print('Sorry, that was not a valid choice.')
            print()
        self.board.mark_square(move, self.human.marker)

    def computer_moves(self):
        valid_choices = self.board.unused_squares()
        match self.difficulty:
            case '1':
                move = self.choose_random(valid_choices)
            case '2':
                move = self.medium_computer_move(valid_choices)
            case '3':
                move = self.hard_computer_move(valid_choices)
            case '4':
                move = self.impossible_computer_move(valid_choices)

        self.board.mark_square(move, self.computer.marker)

    def choose_random(self, empties):
        return choice(empties)

    def medium_computer_move(self, empties):
        move = self.crucial_third(self.human)
        return self.choose_random(empties) if not move else move

    def hard_computer_move(self, empties):
        for player in [self.computer, self.human]:
            move = self.crucial_third(player)
            if move:
                break
        if not move:
            move = '5' if '5' in empties else self.choose_random(empties)
        return move

    def impossible_computer_move(self, empties):
        # Take a winning move if available
        move = self.crucial_third(self.computer)
        if move:
            return move

        # Block opponent's winning move
        move = self.crucial_third(self.human)
        if move:
            return move

        # Use minimax to pick best move
        best_score = -float('inf')
        best_square = None
        for square in empties:
            self.board.mark_square(square, self.computer.marker)
            score = self.minimax(False)
            self.board.mark_square(square, Square.INITIAL_MARKER)
            if score > best_score:
                best_score = score
                best_square = square
        return best_square

    def minimax(self, maximizing):
        # Base cases
        if self.is_winner(self.computer):
            return 1
        if self.is_winner(self.human):
            return -1
        if self.board.is_full():
            return 0

        # Recursive case
        if maximizing:
            best_score = -float('inf')
            for square in self.board.unused_squares():
                self.board.mark_square(square, self.computer.marker)
                score = self.minimax(False)
                self.board.mark_square(square, Square.INITIAL_MARKER)
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for square in self.board.unused_squares():
                self.board.mark_square(square, self.human.marker)
                score = self.minimax(True)
                self.board.mark_square(square, Square.INITIAL_MARKER)
                best_score = min(score, best_score)
            return best_score

    def crucial_third(self, player):
        for line in TTTGame.WIN_LINES:
            if self.board.count_markers(player, line) == 2:
                for key in line:
                    if self.board.is_unused_square(key):
                        return key
        return None

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def is_winner(self, player):
        for line in TTTGame.WIN_LINES:
            if self.three_in_row(player, line):
                return True
        return False

    def play_again(self):
        print()
        print('Fancy another one? y/n')
        answer = input().strip().lower()
        while answer not in TTTGame.VALID_ANSWERS:
            print('Please enter y for "yes" or n for "no"')
            answer = input().strip().lower()
        return answer in TTTGame.VALID_ANSWERS[:2]

    def change_difficulty(self):
        print()
        print('Tough, right? How about lowering the difficulty? y/n')
        answer = input().strip().lower()
        while answer not in TTTGame.VALID_ANSWERS:
            print('Please enter y for "yes" or n for "no"')
            answer = input().strip().lower()
        return answer in TTTGame.VALID_ANSWERS[:2]

    def someone_won(self):
        return self.is_winner(self.human) or self.is_winner(self.computer)

    def three_in_row(self, player, row):
        return self.board.count_markers(player, row) == 3

    def toggle_player(self, player):
        return self.computer if player == self.human else self.human

    def update_score(self):
        if self.is_winner(self.human):
            self.human.score += 1
        elif self.is_winner(self.computer):
            self.computer.score += 1

    def display_welcome_message(self):
        system('clear')
        print('Welcome to Tic Tac Toe!')
        print('Your marker is X, computer\'s marker is O.')
        print(f'Match is played to {TTTGame.WINS_LIMIT} wins. Good luck!')

    def display_round_results(self):
        if self.is_winner(self.human):
            print('You won!')
        elif self.is_winner(self.computer):
            print('Computer won!')
        else:
            print('A tie round.')

        print()
        print('***SCOREBOARD***')
        print(f'PLAYER {self.human.score} : '
              f'{self.computer.score} COMPUTER')

    def display_match_results(self):
        if self.human.score == TTTGame.WINS_LIMIT:
            print('You are a pro! Congratulations on winning the match!')
        else:
            print('We trained him well, huh? Better luck next time.')

    def display_goodbye_message(self):
        system('clear')
        print('Thanks for playing Tic Tac Toe! Goodbye!')

    @staticmethod
    def _join_or(sequence, delimiter=', ', join_word='or'):
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

game = TTTGame()
game.play()
