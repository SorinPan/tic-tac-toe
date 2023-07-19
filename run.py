import random

class GameBoard:
    def __init__(self):
        self.board = ['1', '2', '3', '4', '5', '6', '7', '8,', '9']

        def print_board(self):
            print("------------")
            print("|", self.board[0], "|", self.board[1], "|", self.board[2], "|")
            print("------------")
            print("|", self.board[3], "|", self.board[4], "|", self.board[5], "|")
            print("------------")
            print("|", self.board[6], "|", self.board[7], "|", self.board[8], "|")
            print("------------")
        
        def mark_position(self, position, mark):
            self.board[position] = mark

class GamePlay:
    """
    Represents the gamplay logic
    """
    
    def __init__(self):
        self.board = GameBoard()
        self.first_player = ''
        self.second_player = 'Computer'
        self.first_player_mark = ''
        self.second_player_mark = ''
        self.current_player = ''
        self.current_mark = ''


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
    elif option == "2":
        print("Instructions:\n")
        print("1: Choose your mark(X/O)")
        print("2: Players take turns putting their marks on the empty squares on the board")
        print("3: The first player to get 3 in a row wins.")
    else:
        print("Invalid choice, try again.")

main_menu()
        
