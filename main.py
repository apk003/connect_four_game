import random

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

      print("+---+---+---+---+---+---+---+")
      print("|   |   |   |   |   |   |   |")
      print("| {} | {} | {} | {} | {} | {} | {} |".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
      print("|   |   |   |   |   |   |   |")

    print("+---+---+---+---+---+---+---+\n\n")



class ConnectFour:
    # Represents a game of connect four

    def __init__(self, board):
      self.board = board
      self.turn = None

      self.player = None
      self.opponent = None

      self.run_game()


    def find_space(self,col):
      # Finds the first open space

      valid = False
      row = 5

      if self.board[0][col] != " ":
          # Speeds up calculation for full cols
          return None

      while valid == False:
        if self.board[row][col] != " ":
          row -= 1

        elif row < 0:
          return None

        else:
          valid = True

      return row


    def set_space(self, col, value):
      row = self.find_space(col)
      self.board.add(row,col,value)


    def assess_board(self):
      # Acts as AI
      valid = False

      while valid == False:
          choice = random.randint(0,6) #placeholder

          if self.find_space(choice) != None:
              valid = True

      return choice


    def win_board(self, user):
      # Determines if a player won

      pass


    def run_game(self):
      self.in_progress = True

      while self.turn == None:
        choice = input("Who should start? player or opponent\n")

        if choice == "player" or choice == "opponent":
            self.turn = choice

        else:
          print("Invalid choice.")

      while self.player == None:
        choice = input("Pick x or o\n")

        if choice == 'x':
          self.player = 'x'
          self.opponent = 'o'

        elif choice == 'o':
          self.player = 'o'
          self.opponent = 'x'

        else:
          print("Invalid choice.")

      while self.in_progress == True:
        if self.turn == "player":
          choice = input("Choose an open column. 1 - 7\n")

          try:
              choice = int(choice)

          except TypeError:
              print("Invalid space.")

          else:
              if choice not in [1, 2, 3, 4, 5, 6, 7]:
                print("Invalid space.")

              elif self.find_space(choice-1) == None:
                print("Invalid space.")

              else:
                self.set_space(choice-1, self.player)
                self.board.show()
                self.turn = "opponent"

        else:
          self.set_space(self.assess_board(), self.opponent)
          self.board.show()
          self.turn = "player"


boardd = Board()
game = ConnectFour(boardd)
