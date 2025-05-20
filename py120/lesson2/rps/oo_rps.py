from random import choice

class Player:
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self):
        self.move = None

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = choice(Player.CHOICES)

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt = 'Please choose rock, paper, or scissors: '
        while True:
            move = input(prompt).strip().lower()
            if move in Player.CHOICES:
                break
            print(f'{move} is not a valid choice.')
        self.move = move

class RPSGame:
    PLAY_AGAIN = ('y', 'yes')
    WIN_COMBOS = {'rock': 'scissors',
                  'paper': 'rock',
                  'scissors': 'paper'}

    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _display_winner(self):
        print(f'You chose: {self._human.move}')
        print(f'Computer chose: {self._computer.move}')

        if self._human.move == self._computer.move:
            print('It\'s a tie!')
        elif RPSGame.WIN_COMBOS[self._human.move] == self._computer.move:
            print('You win!')
        else:
            print('Computer wins!')

    def _play_again(self):
        answer = input('Would you like to play again? (y/n) ').strip().lower()
        return answer in RPSGame.PLAY_AGAIN

    def play(self):
        self._display_welcome_message()

        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if not self._play_again():
                break

        self._display_goodbye_message()

RPSGame().play()
