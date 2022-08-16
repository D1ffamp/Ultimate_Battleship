import random

# taken from knowledge mavens youtube tutorial
class Board:
    """
    creates board object and sets size and layout of board
    """
    def __init__(self, board):
        self.board = board

    def convert_letters_to_numbers():
        """
        function to convert the letters on top of board to numbers
        """
        letters_to_numbers = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
            'F': 5,
            'G': 6,
            'H': 7
        }

        return letters_to_numbers

    def print_board(self):
        """
        function to loop through numbers 1 to 8 to populate board
        """
        print("A B C D E F G H")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

class Battleship:
    """ 
    creates class object for the ships and fucntions for user inputs and score 
    """

    def __init__(self, board):
        self.board = board

    def create_ships(self):
        """ 
        function to create the ships
        """
        for i in range(5):
            self.x_row = random.randint(0, 7)
            self.y_column =  random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row,  = random.randint(0, 7)
                self.y_column = random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        
        return self.board

    def get_user_input(self):
        """
        function to allow user input and to check it is valid
        """
        try:
            x_row = input("Enter the row of the ship: ")
            while x_row not in '12345678':
                print('Not an appropriate choice, please select a valid row')
                x_row = input("Enter the row of the ship: ")

            y_column = input("Enter the column letter of the ship: ").upper()
            while y_column not in "ABCDEFGH":
                print('Not an appropriate choice, please select valid column')
                y_column = input("Enter the column letter of ship: ").upper()
            return int(x_row) - 1, Board.convert_letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not a valid input")
        return self.get_user_input()
    
