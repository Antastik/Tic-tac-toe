import player

class Board:
    def __init__(self):
        self.n = 3
        self.board = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.row_sum = [0] * self.n
        self.col_sum = [0] * self.n
        self.diag_sum = 0
        self.rev_diag_sum = 0
        self.current_player = None
        self.moves_history = []
    
    def display(self): 
        print("\n")
        for i in range(self.n):
            row_display = []
            for j in range(self.n):
                if self.board[i][j] == 0:
                    row_display.append(' ')
                elif self.board[i][j] == 1:
                    row_display.append('X')
                else:  
                    row_display.append('O')
            print(f" {row_display[0]} | {row_display[1]} | {row_display[2]} ")
            if i < self.n - 1:
                print("-----------")
        print("\n")
    
    def get_board(self, Board_ID=None):
        return self.board
    