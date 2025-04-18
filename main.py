from game import Game

def print_instructions():
    """Print game instructions for the user."""
    print("\n=== TIC-TAC-TOE ===")
    print("Instructions:")
    print("- Enter row and column numbers (0-2) separated by a space")
    print("- Type 'undo' to undo the last move")
    print("- Type 'reset' to start a new game")
    print("- Type 'quit' to exit the game")
    print("- Type 'stats' to view player statistics")
    print("=====================\n")

def display_stats(game):
    """Display player statistics."""
    p1 = game.p1()
    p2 = game.p2()
    p1_stats = p1.stats()
    p2_stats = p2.stats()
    
    print(f"Player 1 ({p1.symbol()}) stats: Wins: {p1_stats['wins']}, Losses: {p1_stats['losses']}, Draws: {p1_stats['draws']}")
    print(f"Player 2 ({p2.symbol()}) stats: Wins: {p2_stats['wins']}, Losses: {p2_stats['losses']}, Draws: {p2_stats['draws']}")

def main():
    """Main game loop."""
    game = Game()
    print_instructions()
    
    while True:
        game.display()
        print(game.get_status())
        
        if game.is_game_over():
            play_again = input("Play again? (y/n): ").lower()
            if play_again == 'y':
                game.reset_game()
                continue
            else:
                print("Thanks for playing!")
                break
        
        command = input("Enter move (row col), 'undo', 'reset', 'stats', or 'quit': ")
        
        if command.lower() == 'quit':
            print("Thanks for playing!")
            break
        
        elif command.lower() == 'undo':
            if not game.undo():
                print("Cannot undo any further!")
        
        elif command.lower() == 'reset':
            game.reset_game()
            print("Game has been reset.")
            
        elif command.lower() == 'stats':
            display_stats(game)
        
        else:
            try:
                parts = command.split()
                if len(parts) != 2:
                    print("Invalid input! Please enter row and column as two numbers separated by a space.")
                    continue
                    
                row, col = map(int, parts)
                if not (0 <= row < 3 and 0 <= col < 3):
                    print("Invalid input! Row and column must be between 0 and 2.")
                    continue
                
                # Try to make the move
                result = game.switch_player(row, col)
                if not result:
                    print("Invalid move! The cell is already occupied.")
            except ValueError:
                print("Invalid input! Please enter row and column as numbers or a valid command.")

if __name__ == "__main__":
    main()