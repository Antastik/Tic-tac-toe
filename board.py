class Board:
    def __init__(self):
        self.n = 3
        self.board = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.row_sum = [0] * self.n
        self.col_sum = [0] * self.n
        self.diagonal_sum = 0
        self.reverse_diag_sum = 0
        self.curr_player = None
        self.move_history = []
    
    def show_board(self): 
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
    
    def move(self, player_obj, row, col):
        if row < 0 or col < 0 or row >= self.n or col >= self.n:
            return False
        
        if self.board[row][col] != 0:
            return False

        player_val = 1 if player_obj.symbol() == 'X' else -1
        
        # Make the move
        self.board[row][col] = player_val
        self.curr_player = player_obj
        self.move_history.append((player_obj, row, col))

        self.row_sum[row] += player_val
        self.col_sum[col] += player_val

        if row == col:
            self.diagonal_sum += player_val
        if row == self.n - 1 - col:
            self.reverse_diag_sum += player_val

        # Winning Condition
        if (
            abs(self.row_sum[row]) == self.n or 
            abs(self.col_sum[col]) == self.n or
            abs(self.diagonal_sum) == self.n or
            abs(self.reverse_diag_sum) == self.n):
            return True
        
        return None  
    
    def undo_move(self):
        if not self.move_history:
            return False
            
        player_obj, row, col = self.move_history.pop()
        player_val = 1 if player_obj.symbol() == 'X' else -1
        
        # Clear the board position
        self.board[row][col] = 0

        self.row_sum[row] -= player_val
        self.col_sum[col] -= player_val

        if row == col:
            self.diagonal_sum -= player_val
        if row == self.n - 1 - col:
            self.reverse_diag_sum -= player_val
        
        # Update current player to the previous one
        self.curr_player = self.move_history[-1][0] if self.move_history else None
        
        return True
    
    def check_winner(self):
        for i in range(self.n):
            if abs(self.row_sum[i]) == self.n:
                return 'X' if self.row_sum[i] == self.n else 'O'
            
            if abs(self.col_sum[i]) == self.n:
                return 'X' if self.col_sum[i] == self.n else 'O'

        # check diagonals
        if abs(self.diagonal_sum) == self.n:
            return 'X' if self.diagonal_sum == self.n else 'O'
        
        if abs(self.reverse_diag_sum) == self.n:
            return 'X' if self.reverse_diag_sum == self.n else 'O'

        return None
    
    def is_board_full(self):
        for row in range(self.n):
            for col in range(self.n):
                if self.board[row][col] == 0:
                    return False
                
        return True
    
    def get_curr_player(self):
        return self.curr_player
    
    def reset(self):
        self.board = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.row_sum = [0] * self.n
        self.col_sum = [0] * self.n
        self.diagonal_sum = 0
        self.reverse_diag_sum = 0
        self.curr_player = None
        self.move_history = []