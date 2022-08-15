from random import randint

scores = {'computer': 0, 'player': 0}

# board class taken from code institute battleship example
class Board:
    """
    Main board class that sets the board size, the number of ships, the players name, the players board and computer board
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []


    def print(self):
        # prints board
        for row in self.board:
            print("  ".join(row))

    def guess(self, x, y):
        # appends X at the chosen coordinates
        self.board[x][y] = "X"

        # appends * if chosen coordinates hits a target
        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"

def validate_coodinates():
def populate_board():
def make_quess():
def play_game():
def new_game():


