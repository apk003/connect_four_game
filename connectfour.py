import random

class ConnectFour:
    # Represents a game of connect four

    def __init__(self, board):
      self.board = board
      self.turn = None

      self.player = None
      self.opponent = None
      self.turn_count = 0

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


    def won_game(self, user):

        # Checks horizontals
        for col in range(len(self.board[0])):
            for row in range(len(self.board)-3):
                if self.board[row][col] == user and self.board[row+1][col] == user and self.board[row+2][col] == user and self.board[row+3][col] == user:
                    return True

        # Checks verticals
        for row in range(len(self.board)):
            for col in range(len(self.board[0])-3):
                if self.board[row][col] == user and self.board[row][col+1] == user and self.board[row][col+2] == user and self.board[row][col+3] == user:
                    return True

        # Checks diagonals
        for row in range(len(self.board) - 3):
            for col in range(3, len(self.board[0])):
                if self.board[row][col] == user and self.board[row+1][col-1] == user and self.board[row+2][col-2] == user and self.board[row+3][col-3] == user:
                    return True

        # Accounts for filled board
        if self.turn_count == 42:
            return 'tie'


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

                      if self.won_game(self.player):
                          print("You have won!")
                          self.in_progress = False

                      elif self.won_game(self.player) == 'tie':
                          print("It's a tie!")
                          self.in_progress = False


          else:
            self.set_space(self.assess_board(), self.opponent)
            self.board.show()
            self.turn = "player"

            if self.won_game(self.opponent):
                print("You have lost!")
                self.in_progress = False

            elif self.won_game(self.opponent) == 'tie':
                print("It's a tie!")
                self.in_progress = False
