# Manages teh overall flow
class Game:
    def __init__(self, board, player1, player2, current_player) -> None:
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.current_player = current_player
        
    # Switch currently Player
    def switch_player(self) -> None:
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        
    # Game loop
    def play(self) -> None:
        while True:
            self.board.display()
            self.current_player.get_move(self.board)
            
            if self.board.is_full():                            # Tie Game
                print("Tie game!")
                break
            
            elif self.board.check_winner():                     # Check for winner
                print(f"{self.current_player.name} wins!")                
                break
            self.switch_player()                                # Switch current_player