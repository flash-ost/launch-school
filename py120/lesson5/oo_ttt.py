from os import system
from random import choice

class Square:
    INITIAL_MARKER = ' '
    HUMAN_MARKER = 'X'
    COMPUTER_MARKER = 'O'

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    @property
    def square(self):
        return self._marker

    @square.setter
    def square(self, marker):
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
        print()
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

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    VALID_ANSWERS = ('y', 'n')
    WIN_LINES = ('123', '456', '789', # rows
                 '147', '258', '369', # columns
                 '159', '357')        # diagonals
    WINS_LIMIT = 3

    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self.reset_scores()

    def host_match(self):
        while True:
            self.host_game()
            if TTTGame.WINS_LIMIT in self.scores.values():
                break
            input('Press ENTER when ready for the next round: ')
            system('clear')
            self.board.reset()
        self.display_match_results()    

    def host_game(self):    
        self.board.display()
        while True:
            self.human_moves()
            if self.is_game_over():
                system('clear')
                self.board.display()
                break

            self.computer_moves()
            system('clear')
            self.board.display()
            if self.is_game_over():
                break
        self.display_game_results()

    def play(self):
        self.display_welcome_message()
        while True:
            self.host_match()
            if not self.play_again():
                break
            system('clear')
            print("Let's play again!")
            self.board.reset()
            self.reset_scores()

        self.display_goodbye_message()

    def display_welcome_message(self):
        system('clear')
        print('Welcome to Tic Tac Toe!')

    def display_goodbye_message(self):
        system('clear')
        print('Thanks for playing Tic Tac Toe! Goodbye!')

    def display_game_results(self):
        if self.is_winner(self.human):
            self.scores['human'] += 1
            print('You won! Congratulations!')
        elif self.is_winner(self.computer):
            self.scores['computer'] += 1
            print('I won! I won! Take that, human!')
        else:
            print('A tie game. How boring.')

        print('***SCOREBOARD***')
        print(f'PLAYER {self.scores['human']} : {self.scores['computer']} COMPUTER')

    def display_match_results(self):
        if self.scores['human'] == TTTGame.WINS_LIMIT:
            print('You are a pro! Congratulations on winning the match!')
        else:
            print('We trained him well, huh? Better luck next time.')

    def human_moves(self):
        valid_choices = self.board.unused_squares()
        choices_str = self._join_or(valid_choices)
        prompt = f'Choose a square ({choices_str}): '
        while True:
            move = input(prompt)
            if move in valid_choices:
                break

            print('Sorry, that was not a valid choice.')
            print()
        self.board.mark_square(move, self.human.marker)

    def computer_moves(self):
        valid_choices = self.board.unused_squares()
        move = choice(valid_choices)
        self.board.mark_square(move, self.computer.marker)

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def is_winner(self, player):
        for line in TTTGame.WIN_LINES:
            if self.three_in_row(player, line):
                return True
        return False
    
    def play_again(self):
        while True:
            print()
            print('Fancy another one? y/n')
            answer = input().strip().lower()
            if answer in TTTGame.VALID_ANSWERS:
                break
        return answer == TTTGame.VALID_ANSWERS[0]
    
    def reset_scores(self):
        self.scores = {'human': 0,
                       'computer': 0}

    def someone_won(self):
        return self.is_winner(self.human) or self.is_winner(self.computer)

    def three_in_row(self, player, row):
        return self.board.count_markers(player, row) == 3
    
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
