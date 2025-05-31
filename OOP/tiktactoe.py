from board import Board
from player import Player
from game import Game

# Main logic for overall flow
def main():
    board = Board()
    player1 = Player()
    player2 = Player()
    
    player1.player_setup()
    player2.player_setup()
    
    game = Game(board, player1, player2, player1)
    
    while True:
        game.play()
        
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break
        board.reset_board()
        Player.used_markers = []
        
# Only runs if compiler is running main
if __name__ == "__main__":
    main()