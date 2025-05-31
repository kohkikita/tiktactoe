# Base class for player
class Player:
    used_markers = [] # Keeps track of used markers
    def __init__(self, name=None, marker=None) -> None:
        self.marker = marker
        self.name = name
        pass
    
    # Setup for player: name & marker
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
            
    # Printing out user name and marker
    def player_info(self) -> None:
        print(f"{self.name} ({self.marker})")          
                
    # Prompts user for move         
    def get_move(self, board) -> None:
        print(f"{self.player_info()}'s turn")
        
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