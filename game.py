import player
import board

class Game:
    def __init__(self):
        self.board = board.Board()
        self.player1 = player.Player(1, 'X')
        self.player2 = player.Player(2, 'O')
        self.curr_player = self.player1
        self.game_over = False
        self.winner = None
     
    def p1(self):
        pass

    def p2(self):
        pass