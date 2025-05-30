"""
Question 1
Suppose you have these two classes:

class Game:
    def play(self):
        return 'Start the game!'

class Bingo:
    pass
Update this code so that Bingo inherits the play method from the Game class.
"""
class Game:
    def play(self):
        return 'Start the game!'

class Bingo(Game):
    pass

print(Bingo().play())