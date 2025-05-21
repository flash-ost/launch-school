from random import choice
from os import system

class PromptMixin():
    def _prompt(self, message):
        print(f'==> {message}')

class Player:
    CHOICES = {
        'r': 'rock',
        'p': 'paper',
        'sc': 'scissors',
        'l': 'lizard',
        'sp': 'spock',
    }

    def __init__(self, game=None):
        self.move = None
        self._game = game

class HandyAndy(Player):
    def __init__(self, game=None):
        super().__init__(game)

    def choose(self):
        self.move = choice(tuple(Player.CHOICES.values()))

class R2D2(Player):
    def __init__(self, game=None):
        super().__init__(game)

    def choose(self):
        self.move = 'rock'

class HAL(Player):
    def __init__(self, game=None):
        super().__init__(game)

    def choose(self):
        self.move = choice(['scissors'] * 5 + list(Player.CHOICES.values()))

class Daneel(Player):
    def __init__(self, game=None):
        super().__init__(game)

    def choose(self):
        human_moves = self._game.moves['human']
        self.move = human_moves[-1] if human_moves \
            else choice(tuple(Player.CHOICES.values()))

class Human(PromptMixin, Player):
    def __init__(self, game=None):
        super().__init__(game)

    def choose(self):
        self._prompt(f'Choose one: {', '.join(Player.CHOICES.values())}')
        self._prompt(
            f'You can also type abbreviated names: '
            f'{', '.join(Player.CHOICES)}'
        )

        while True:
            move = input().strip().lower()
            if move in Player.CHOICES or move in Player.CHOICES.values():
                break
            self._prompt('Invalid choice.')

        if len(move) <= 2:
            move = Player.CHOICES[move]
        self.move = move

class RPSGame(PromptMixin):
    PLAY_AGAIN = ('y', 'yes')
    COMPUTERS = (HandyAndy, R2D2, HAL, Daneel)
    WIN_COMBOS = {
        'rock':     ['scissors', 'lizard'],
        'paper':    ['rock',     'spock'],
        'scissors': ['paper',    'lizard'],
        'lizard':   ['paper',    'spock'],
        'spock':    ['rock',     'scissors'],
        }
    WIN_SCORE = 5

    def __init__(self):
        self._human = Human()
        self._computer = None
        self.moves = None
        self._results = None
        self._scoreboard = None

    def _display_welcome_message(self):
        system('clear')
        self._prompt('Welcome to Rock Paper Scissors!')
        self._prompt(
            """The rules are (not so) simple:
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
        self._prompt(
            f'The game is played to {RPSGame.WIN_SCORE} wins, '
            f'ties don\'t count.'
        )
        self._prompt('Press ENTER when ready.')
        input()

    def _display_goodbye_message(self):
        system('clear')
        self._prompt('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _host_round(self):
        self._human.choose()
        self._computer.choose()
        self._record_moves()
        self._display_round_summary(self._resolve_round())

    def _record_moves(self):
        self.moves['human'].append(self._human.move)
        self.moves['computer'].append(self._computer.move)

    def _resolve_round(self):
        if self._human.move == self._computer.move:
            self._results.append('Tie')
            return 'It\'s a tie!'
        if self._computer.move in RPSGame.WIN_COMBOS[self._human.move]:
            self._scoreboard['human'] += 1
            self._results.append('You')
            return 'You win!'
        self._scoreboard['computer'] += 1
        self._results.append(f'{type(self._computer).__name__}')
        return f'{type(self._computer).__name__} wins!'

    def _display_round_summary(self, message):
        system('clear')
        self._prompt(f'You chose: {self._human.move}')
        self._prompt(
            f'{type(self._computer).__name__} '
            f'chose: {self._computer.move}'
        )
        self._prompt(message)

        human_score = self._scoreboard['human']
        computer_score = self._scoreboard['computer']
        computer_name = type(self._computer).__name__.upper()
        print(f'PLAYER {human_score} : {computer_score} {computer_name}')
        print()

    def _host_game(self):
        self._prepare_game()
        self._announce_opponent()
        while RPSGame.WIN_SCORE not in self._scoreboard.values():
            self._host_round()
        self._display_game_summary()

    def _announce_opponent(self):
        system('clear')
        self._prompt(
            f'You are playing against '
            f'{type(self._computer).__name__}. Good luck!'
        )

    def _display_game_winner(self):
        if self._scoreboard['human'] == RPSGame.WIN_SCORE:
            self._prompt(
                'You\'re a natural! '
                'Congratulations on winning the game!'
            )
        else:
            self._prompt(
                f'We trained {type(self._computer).__name__} well, huh? '
                f'Better luck next time.'
            )

    def _display_moves(self):
        self._prompt(
            f'Here are your and {type(self._computer).__name__}\'s '
            f'moves thoughout the game:'
        )
        print(
            f'{'ROUND':<8}{'PLAYER':<10}'
            f'{type(self._computer).__name__.upper():<10}WINNER'
        )
        for i in range(len(self.moves['human'])):
            human = self.moves['human'][i]
            computer = self.moves['computer'][i]
            result = self._results[i]
            print(f'{i+1:<8}{human:<10}{computer:<10}{result}')

    def _display_game_summary(self):
        self._display_game_winner()
        self._display_moves()

    def _play_again(self):
        print()
        self._prompt('Would you like to play again? (y/n)')
        answer = input().strip().lower()
        return answer in RPSGame.PLAY_AGAIN

    def _prepare_game(self):
        self._computer = choice(RPSGame.COMPUTERS)(self)
        self.moves = {
            'human': [],
            'computer': [],
            }

        self._results = []
        self._scoreboard = {
            'human': 0,
            'computer': 0,
        }

    def play(self):
        self._display_welcome_message()

        while True:
            self._host_game()
            if not self._play_again():
                break
            system('clear')
        self._display_goodbye_message()

RPSGame().play()
