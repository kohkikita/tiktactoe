# Holds and displays current state
class Board:    
    def __init__(self) -> None:
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        
        # For testing
        # self.board = [["1", "1", "1"],
        #               ["1", "1", "1"],
        #               ["1", "1", "1"]]
        
    # Reset board for new game
    def reset_board(self) -> None:
        self.board = [[" " for _ in range(3)] for _ in range(3)]
            
    # Print out board
    def display(self) -> None:
        for i in range(3):
            print(" | ".join(self.board[i]))
        print("-"*9)
            
    # Place corresponding marker on board
    def place_marker(self, row: int, col: int, marker: str) -> None:
        if self.is_valid_move(row, col):
            # -1 for user entry 
            self.board[row][col] = marker
    
    # Checks if box is available
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
    
    # Checks if the board is full for tie game
    def is_full(self) -> bool:
        return all(cell != " " for row in self.board for cell in row)