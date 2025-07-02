from random import shuffle
from os import system

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:
    SUITS = '♠♥♦♣'
    VALUES = { '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
           '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11, }

    def __init__(self):
        self.reset()

    def reset(self):
        self.cards = [Card(suit, value) for suit in Deck.SUITS
                                        for value in Deck.VALUES]
        shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Player():
    def __init__(self):
        self.credits = TwentyOneGame.CREDIT_LIMIT
        self.hand = []
        self.hand_value = 0

    def reset_hand(self):
        self.hand = []
        self.hand_value = 0

    def take_card(self, card):
        self.hand.append(card)
        self.update_hand_value()

    def update_hand_value(self):
        values = [card.value for card in self.hand]
        value_sum = 0

        for value in values:
            value_sum += Deck.VALUES[value]

        aces = values.count('A')
        while value_sum > TwentyOneGame.MAX_HAND and aces:
            value_sum -= 10
            aces -= 1

        self.hand_value = value_sum

    def is_busted(self):
        return self.hand_value > TwentyOneGame.MAX_HAND

class Dealer(Player):
    HIT_CAP = 17

class TwentyOneGame:
    CREDIT_LIMIT = 3
    MAX_HAND = 21
    VALID_ANSWERS = ('n', 'no', 'y', 'yes')
    VALID_MOVES = ('h', 'hit', 's', 'stay')

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def host_game(self):
        while True:
            self.deal_initial()
            self.show_cards()
            self.player_turn()
            if not self.player.is_busted():
                self.dealer_turn()
            self.wrap_round()

            if self.player.credits == 0 or self.dealer.credits == 0:
                self.display_game_result()
                break
            self.prepare_round()

    def play(self):
        self.display_welcome_message()
        while True:
            self.host_game()
            if not self.play_again():
                break
            print('Sure, let\'s play again!')
            self.reset_credits()
            self.prepare_round()
        self.display_goodbye_message()

    def deal_initial(self):
        for _ in range(2):
            self.player.take_card(self.deck.deal())
            self.dealer.take_card(self.deck.deal())

    def show_cards(self, final_display=False):
        system('clear')
        for player in (self.dealer, self.player):
            rows = ['', '', '', '', '']
            print(f'{player.__class__.__name__.upper()}\'S HAND')
            hand = player.hand

            # If not final display, second dealer's card should be face down
            if isinstance(player, Dealer) and not final_display:
                hand = [hand[0], Card('?', '?')]
            for card in hand:
                value_top = card.value if card.value == '10' \
                    else f'{card.value} '
                value_bottom = card.value if card.value == '10' \
                    else f' {card.value}'
                rows[0] += '+-----+  '
                rows[1] += f'|{value_top}   |  '
                rows[2] += f'|  {card.suit}  |  '
                rows[3] += f'|   {value_bottom}|  '
                rows[4] += '+-----+  '

            for row in rows:
                print(row)

    def player_turn(self):
        while True:
            if self.player.is_busted():
                return

            self.show_cards()
            print(f'Your hand value is {self.player.hand_value}')
            print('Do you want to hit or stay? h/s')
            move = input().strip().lower()
            while move not in TwentyOneGame.VALID_MOVES:
                print('Please enter h for "hit" or s for "stay":')
                move = input().strip().lower()

            if move in TwentyOneGame.VALID_MOVES[:2]:
                self.player.take_card(self.deck.deal())
            else:
                return

    def dealer_turn(self):
        while self.dealer.hand_value < Dealer.HIT_CAP:
            self.dealer.take_card(self.deck.deal())

    def wrap_round(self):
        message, winner, loser = self.determine_round_outcome()
        if winner and loser:
            self.update_credits(winner, loser)
        self.display_round_result(message)

    def determine_round_outcome(self):
        if self.player.is_busted():
            return ('You busted, dealer wins!', self.dealer, self.player)
        if self.dealer.hand_value > TwentyOneGame.MAX_HAND:
            return ('Dealer busted, you win!', self.player, self.dealer)
        if self.player.hand_value > self.dealer.hand_value:
            return ('Your hand is higher, you win!', self.player, self.dealer)
        if self.player.hand_value < self.dealer.hand_value:
            return ('Dealer\'s hand is higher, you lose!',
                    self.dealer, self.player)
        return ('It\'s a tie!', None, None)

    def display_welcome_message(self):
        system('clear')
        print('Let\'s play Twenty-One!')
        print(f'Both you and dealer get '
              f'a ${TwentyOneGame.CREDIT_LIMIT} credit.')
        print('Game ends when one of the players has no credit left.'
              'Good luck!')
        input('Press ENTER when ready: ')

    def display_goodbye_message(self):
        system('clear')
        print('Thank you for playing! Goodbye!')

    def display_round_result(self, message):
        self.show_cards(True)
        print(f'Your hand value is {self.player.hand_value}')
        if not self.player.is_busted():
            print(f"Dealer's hand value is {self.dealer.hand_value}")
        print(message)

        print()
        print('CREDIT BALANCES')
        print(f'You: ${self.player.credits}')
        print(f'Dealer: ${self.dealer.credits}')

    def display_game_result(self):
        if self.player.credits == 0:
            print('You lost all your credits. Better luck next time.')
        else:
            print('Dealer is out of credits. Congratulations!')

    def update_credits(self, winner, loser):
        winner.credits += 1
        loser.credits -= 1

    def reset_credits(self):
        self.player.credits = TwentyOneGame.CREDIT_LIMIT
        self.dealer.credits = TwentyOneGame.CREDIT_LIMIT

    def prepare_round(self):
        self.deck.reset()
        self.player.reset_hand()
        self.dealer.reset_hand()

        print()
        input('Press ENTER when ready for the next round: ')

    def play_again(self):
        print()
        print('Fancy another game? y/n')
        answer = input().strip().lower()
        while answer not in TwentyOneGame.VALID_ANSWERS:
            print('Please enter y for "yes" or n for "no"')
            answer = input().strip().lower()
        return answer in TwentyOneGame.VALID_ANSWERS[2:]

game = TwentyOneGame()
game.play()