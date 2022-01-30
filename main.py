from board import *
from connectfour import *

print("  ┎──────────────┒\n  ┃ Connect Four ┃\n  ┖──────────────┚\n")

while True:
    print("Select a game:")
    game = input("Original\n\n")

    while game.lower() == "original":
        new_board = Board()
        new_game = ConnectFour(new_board)

        if input("Play again? y/n\n").lower() == "n":
            if input("Quit to game select? y/n\n").lower() == "y":
                game = "select"

            else:
                print("Resetting data...\n")
        else:
            print("Resetting data...\n")
