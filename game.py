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
        return self.player1

    def p2(self):
        return self.player2
    
    def switch_player(self, row, col):
        if self.game_over:
            return False
        
        move_result = self.board.move(self.curr_player, row, col)
        if move_result is False:
            return False
        
        if move_result is True:
            self.game_over = True
            self.winner = self.curr_player

            if self.winner == self.player1:
                self.player1.add_win()
                self.player2.add_loss()
            else:
                self.player2.add_win()
                self.player1.add_loss()

            return True
        
        # Checking for draw
        if self.board.is_board_full():
            self.game_over = True
            self.player1.add_draw()
            self.player2.add_draw()
            return True
        
    def undo(self):
        if self.board.undo_move():
            if self.game_over:
                self.game_over = False
                self.winner = None
            else:
                self.switch_player()
            return True
        return False
    
    def reset_game(self):
        self.board.reset()
        self.curr_player = self.player1
        self.game_over = False
        self.winner = None

    def get_status(self):
        if self.game_over:
            if self.winner:
                return f"Game over ! Player {self.winner.player_id()} ({self.winner.symbol()}) wins!"
            else:
                return "Game over! It's a draw!"
        else:
            return f"Player {self.current_player.player_id()} ({self.current_player.symbol()})'s turn"
        
    def display(self):
        self.board.show_board()

    def is_game_over(self):
        return self.game_over