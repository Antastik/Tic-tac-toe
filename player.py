class Player:
    def __init__(self, player_id, symbol) -> None:
        self.id = player_id
        self.sym = symbol
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def player_id(self):
        return self.id

    def symbol(self):
        return self.sym

    def stats(self):
        return {
            "wins": self.wins,
            "losses": self.losses,
            "draws": self.draws
        }
    
    def add_win(self):
        self.wins += 1
    
    def add_loss(self):
        self.losses += 1
    
    def add_draw(self):
        self.draws += 0



        
    