import random


class GameBoard:
    def __init__(self):
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def print_board(self):
        print("------------")
        print("|", self.board[0], "|", self.board[1], "|", self.board[2], "|")
        print("------------")
        print("|", self.board[3], "|", self.board[4], "|", self.board[5], "|")
        print("------------")
        print("|", self.board[6], "|", self.board[7], "|", self.board[8], "|")
        print("------------")

    def mark_position(self, position, mark):
        """
        Adds the player's or computer's move to the board
        """

        self.board[position] = mark

    def is_position_free(self, position):
        """
        Checks if the square chosen on the gameboard is free
        """
        return self.board[position].isdigit()
    
    def is_board_full(self):
        """
        Checks if the board is full
        """

        for x in self.board:
            if x.isdigit():
                return False
        return True
    
    def is_player_winner(self, mark):
        """
        Checks if the current player is the winner
        """
        
        win_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Row combinations
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Column combinations
            [0, 4, 8], [2, 4, 6] # Diagonal combinations
        ]

        for combo in win_combos:
            all_match = True
            for pos in combo:
                if self.board[pos] != mark:
                    all_match = False
                    break
            
            if all_match:
                return True
        
        return False


class GamePlay:
    """
    Represents the gamplay logic
    """

    def __init__(self):
        self.board = GameBoard()
        self.first_player = ""
        self.second_player = "Computer"
        self.first_player_mark = ""
        self.second_player_mark = ""
        self.current_player = ""
        self.current_mark = ""

    def play_game(self):
        """
        Controls the game flow
        """

        self.board.print_board()
        self.initiate_players()

        while True:
            print(f"It's {self.current_player}'s turn ({self.current_mark})")
            
            position = self.get_next_move()
            self.board.mark_position(position, self.current_mark)
            self.board.print_board

            if self.board.is_player_winner(self.current_mark):
                print(f"{self.current_player} is the winner!")
                break
            
            if self.board.is_board_full():
                print("Game over! It's a tie!\n")
                break
        
        self.switch_player()

    def initiate_players(self):
        """
        Initializes players. Takes in player's name and their choice of mark
        """

        self.first_player = input("Enter First Player name: ")
        mark = input("Choose your mark (X/O): ")

        if mark == "X":
            self.first_player_mark = "X"
            self.second_player_mark = "O"
        else:
            self.first_player_mark = "O"
            self.second_player_mark = "X"
        
        self.current_player = random.choice([self.first_player, self.second_player])
        
        if self.current_player == self.first_player:
            self.current_mark = self.first_player_mark
        else:
            self.current_mark = self.second_player_mark
    
    def get_next_move(self):
        while True:
            if self.current_player == self.first_player:
                position = int(input("Enter your move (1-9): ")) - 1
            else:
                avail_positions = [i for i, x in enumerate(self.board.board) if x.isdigit()]
                position = random.choice(avail_positions)
            
            if self.board.is_position_free(position):
                return position
            else:
                print("Invalid move! Please try again.")
    
    def switch_player(self):
        """
        Switch between players
        """

        if self.current_player == self.second_player:
            self.current_player = self.first_player
        else:
            self.current_player = self.second_player
        
        if self.current_mark == self.second_player_mark:
            self.current_mark = self.first_player_mark
        else:
            self.current_mark = self.second_player_mark


def main_menu():
    """
    Displays the Main Menu. Where the user can choose between
    starting the game or show the instructions
    """

    print("Welcome to a classic game of Tic-Tac-Toe!\n")
    print("1: Start Game")
    print("2: Instructions")

    option = input("Enter: 1/2\n")

    if option == "1":
        start_game = GamePlay()
        start_game.play_game()
    elif option == "2":
        print("Instructions:\n")
        print("1: Choose your mark(X/O)")
        print(
            "2: Players take turns putting their marks on the empty squares on the board"
        )
        print("3: The first player to get 3 in a row wins.")
    else:
        print("Invalid choice, try again.")


main_menu()
