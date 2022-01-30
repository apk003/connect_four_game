class Board:
  # Represents a connect four board

    def __init__(self, board_data=[]):

        self.clean_board = [
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            ]

        if board_data == []:
            self.data = self.clean_board

        else:
            self.data = board_data


    def __getitem__(self,key):
        return self.data[key]

    def __len__(self):
        return len(self.data)


    def add(self, row, col, value):
        # Adds to board
        self.data[row][col] = value


    def clear(self):
        # Clears board
        self.data = self.clean_board


    def show(self):
        # Displays board

        print("  1   2   3   4   5   6   7")
        for row in self.data:

            print("╋───╋───╋───╋───╋───╋───╋───╋")
            print("┃   ┃   ┃   ┃   ┃   ┃   ┃   ┃")
            print("┃ {} ┃ {} ┃ {} ┃ {} ┃ {} ┃ {} ┃ {} ┃".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            print("┃   ┃   ┃   ┃   ┃   ┃   ┃   ┃")

        print("╋───╋───╋───╋───╋───╋───╋───╋\n\n")
