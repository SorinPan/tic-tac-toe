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


