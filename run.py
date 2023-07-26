import random
import datetime
import gspread
import os
from google.oauth2.service_account import Credentials
from gspread.exceptions import GSpreadException, APIError, WorksheetNotFound

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('tic-tac-toe')

score = SHEET.worksheet('score')


class GameBoard:
    def __init__(self):
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def print_board(self):
        print("-----------------------")
        print("|      |       |      |")
        print(f"|  {self.board[0]}   |   {self.board[1]}   |   {self.board[2]}  |")
        print("|      |       |      |")
        print("-------+-------+-------")
        print("|      |       |      |")
        print(f"|  {self.board[3]}   |   {self.board[4]}   |   {self.board[5]}  |")
        print("|      |       |      |")
        print("-------+-------+-------")
        print("|      |       |      |")
        print(f"|  {self.board[6]}   |   {self.board[7]}   |   {self.board[8]}  |")
        print("|      |       |      |")
        print("-----------------------")

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
    
    def reset_game_board(self):
        """
        Resets the game board so the user can play a new round
        """

        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


class GamePlay:
    """
    Represents the gamplay logic
    """

    def __init__(self):
        self.board = GameBoard()
        self.first_player = ""
        self.second_player = ""
        self.first_player_mark = ""
        self.second_player_mark = ""
        self.current_player = ""
        self.current_mark = ""
        self.rounds_played = 0
        self.first_player_score = 0
        self.second_player_score = 0

    def play_game(self):
        """
        Controls the game flow
        """
        self.board.print_board()
        self.initiate_players()

        while self.rounds_played < 5:
            self.display_score()
            self.board.reset_game_board()
            self.clear_terminal()
            self.board.print_board()

            while True:
                print(f"It's {self.current_player}'s turn ({self.current_mark})")
                position = self.get_next_move()
                self.board.mark_position(position, self.current_mark)
                self.clear_terminal()
                self.board.print_board()

                if self.board.is_player_winner(self.current_mark):
                    print(f"{self.current_player} is the winner!")
                    self.update_score(self.current_player)
                    break
            
                if self.board.is_board_full():
                    print("Game over! It's a tie!\n")
                    break
        
                self.switch_player()
            
            self.rounds_played += 1
        
        print("Game Over!")
        self.game_over(self.first_player, self.second_player, self.first_player_score, self.second_player_score)

    def initiate_players(self):
        """
        Initializes players. Takes in player's name and their choice of mark
        """

        self.first_player = input("Enter First Player name: ")
        player_choice = input("Would you like to play against computer? (y/n): \n")

        if player_choice.lower() == "n":
            self.second_player = input("Enter Second Player name: ")
        else:
            self.second_player = "Computer"

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
    
    def get_human_move(self):
        while True:
            try:
                position = int(input(f"{self.current_player}, enter your move (1-9): ")) - 1

                if 0 <= position < 9:
                    if self.board.is_position_free(position):
                        return position
                    else:
                        print("Invalid move! Please try again.")
                else:
                    print("Invalid input! Please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 9.")
    
    def get_computer_move(self):
        avail_positions = [i for i, x in enumerate(self.board.board) if x.isdigit()]
        position = random.choice(avail_positions)
        return position
    
    def get_next_move(self):
        if self.current_player == self.first_player:
            return self.get_human_move()
        else:
            if self.second_player == "Computer":
                return self.get_computer_move()
            else:
                return self.get_human_move()
    
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
    
    def update_score(self, winner):
        if winner == self.first_player:
            self.first_player_score += 1
        elif winner == self.second_player:
            self.second_player_score += 1
    
    def display_score(self):
        print(f"Round {self.rounds_played + 1} - Current Score:")
        print(f"{self.first_player}: {self.first_player_score}")
        print(f"{self.second_player}: {self.second_player_score}")
    
    def update_google_sheet(self, winner_name, winner_score):
        """
        Updates the worksheet with the winner's name, score and date
        """
        print("Updating score...")
        try:
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            score.append_row([winner_name, winner_score, current_date])
            print("Score updated successfully!")
        except (GSpreadException, APIError, WorksheetNotFound) as e:
            print(f"Something went wrong. Score was not save: {e}") 
    
    def display_top_scores(self):
        """
        Takes the scores from the worksheet and sorts them from highest to lowest
        and displays the top 10 highest
        """
        try:
            score_data = score.get_all_records()
            sorted_scores = sorted(score_data, key=lambda x: x['SCORE'], reverse=True)

            print("Top 10 Highest Scores:")
            print("-----------------------")
            for i, entry in enumerate(sorted_scores[:10], start=1):
                print(f"{i}. {entry['NAME']}: {entry['SCORE']} {entry['DATE']}")
        except (GSpreadException, APIError, WorksheetNotFound) as e:
            print(f"Something went wrong. Top Score can't be displayed: {e}")
    
    def game_over(self, first_player_name, second_player_name, first_player_score, second_player_score):
        """
        Displays the final score between the players, calls the update_google_sheet
        and display_top_scores. Asks the players if they want to play again.
        """

        print("Game Over!")
        print("Final Score:")
        print(f"{self.first_player}: {self.first_player_score}")
        print(f"{self.second_player}: {self.second_player_score}")

        if first_player_score > second_player_score:
            print(f"Congratulations, {self.first_player}! You WON the game!")
            self.update_google_sheet(self.first_player, self.first_player_score)
        elif first_player_score < second_player_score:
            print(f"Congratulations, {self.second_player}! You WON the game!")
            self.update_google_sheet(second_player_name, second_player_score)
        else:
            print("It's a tie")
        
        self.display_top_scores()

        play_again = input("Would you like to play again? (y/n): ")
        if play_again.lower() == "y":
            main_menu
        else:
            print("Thank you for playing!")
    

    def clear_terminal(self):
        """
        Clears the terminal screen before displaying the game board again
        """
        os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    """
    Displays the Main Menu. Where the user can choose between
    starting the game or show the instructions
    """

    print("Welcome to a classic game of Tic-Tac-Toe!\n")
    print("1: Start Game")
    print("2: Instructions")

    try:
        option = input("Enter: 1/2\n")

        if option == "1":
            start_game = GamePlay()
            start_game.play_game()
        elif option == "2":
            print("Instructions:\n")
            print("1: Choose your mark(X/O)")
            print("2: Players take turns putting their marks on the empty squares on the board")
            print("3: The first player to get 3 in a row wins.")
        else:
            print("Invalid choice, try again.")
    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    main_menu()
