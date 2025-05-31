# Manages teh overall flow
class Game:
    def __init__(self, board, player1, player2, current_player) -> None:
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.current_player = current_player
        
    def switch_player(self) -> None:
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        
    def play(self) -> None:
        while True:
            self.board.display()
            self.current_player.get_move(self.board)
            if self.board.is_full():
                print("Tie game!")
                break
            
            elif self.board.check_winner():
                print(f"{self.current_player.name} wins!")
                
                # Add reset function here
                
                break
            self.switch_player()
                
                

# Holds and displays current state
class Board:    
    def __init__(self) -> None:
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        
        # For testing
        # self.board = [["1", "1", "1"],
        #               ["1", "1", "1"],
        #               ["1", "1", "1"]]
        
    def reset_board(self) -> None:
        self.board = [[" " for _ in range(3)] for _ in range(3)]
            
    def display(self) -> None:
        for i in range(3):
            print(" | ".join(self.board[i]))
        print("-"*9)
            
    def place_marker(self, row: int, col: int, marker: str) -> None:
        if self.is_valid_move(row, col):
            # -1 for user entry 
            self.board[row][col] = marker
    
    def is_valid_move(self, row: int, col: int) -> bool:
        if self.board[row][col] != " ":
            return False
        return True

    # determine the winnner by checking player game attribute
    def check_winner(self) -> bool:
        # Checking for row wins
        for row in self.board:
            if len(set(row)) == 1 and row[0] != " ":
                return True
            
        # Checking for column wins
        for col in range(3):
            col_vals = [row[col] for row in self.board]
            if len(set(col_vals)) == 1 and col_vals[0] != " ":
                return True
            
        # Checking for diagnal wins
        diag = [self.board[i][i] for i in range(3)]
        if len(set(diag)) == 1 and diag[0] != " ":
            return True

            
        diag = [self.board[2- i][i] for i in range(3)]
        if len(set(diag)) == 1 and diag[0] != " ":
            return True

        
        return False
    
    def is_full(self) -> bool:
        return all(cell != " " for row in self.board for cell in row)
    
# Base class for player
class Player:
    used_markers = []
    def __init__(self, name=None, marker=None) -> None:
        self.marker = marker
        self.name = name
        pass
    
    def player_setup(self) -> None:
        self.name = input("What is your name: ")
        
        while True:
            marker = input("Enter your symbol: ")
            if len(marker) != 1:
                print("Invalid input. Please enter only one letter.")
            elif marker in Player.used_markers:
                print("The symbol is already taken. Please try again.")
            else:
                self.marker = marker
                Player.used_markers.append(marker)
                break
            
    # For Testing
    def player_info(self) -> None:
        print(f"{self.name} ({self.marker})")          
                
            
    def get_move(self, board) -> None:
        print(f"{self.name}'s turn!")
        
        while True:
            try:
                row = int(input("Enter row #(1-3): ")) - 1
                col = int(input("Enter column #(1-3): ")) - 1
                
                if row not in [0, 1, 2] or col not in [0, 1, 2]:
                    print("Please enter number between 1-3.")
                    continue
                
                if board.is_valid_move(row, col):
                    board.place_marker(row, col, self.marker)
                    break
                else:
                    print("Space is already taken. Try again.")
            except ValueError:
                print("Please enter valid numbers.")

            
    
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
        
        
   
    
if __name__ == "__main__":
    main()