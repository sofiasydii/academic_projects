'''Create a Python program that simulates a simplified version of the Battleship game.
Your program should:
Generate a 10×10 game board.
Randomly place 5 one-mast ships on the board (each ship occupies one unique cell).
Allow the player to guess the location of the ships by entering coordinates (row and column).
Reveal hits and misses on the board:
"." – unrevealed cell
"X" – hit ship
"O" – missed shot
Keep track of the number of moves.
End the game when all ships are sunk and display the number of moves the player used.
The program must include at least the following functions:
set_ships() – randomly generates coordinates for one-mast ships and returns a set of those coordinates.
print_board(board) – displays the current state of the board.
game() – runs the game loop until all ships are sunk, interacting with the player and printing messages.
'''



import random

SHIPS = 5  

def print_board(board):
    print("\n  " + " ".join(str(i) for i in range(10)))
    for i in range(10):
        print(f"{i} " + " ".join(board[i]))
    print()

def set_ships():
    ships = set()
    while len(ships) < SHIPS:
        row = random.randint(0, 10 - 1)
        col = random.randint(0, 10 - 1)
        ships.add((row, col))
    return ships

def game():
    board = [['.' for _ in range(10)] for _ in range(10)]
    hits = set()
    ships = set_ships()
    move_count = 0

    while len(hits) < SHIPS:
        print_board(board)

        try:
            row = int(input("Enter row (0-9): "))
            col = int(input("Enter column (0-9): "))
        except ValueError:
            print("Please enter integers.\n")
            continue

        if not (0 <= row < 10 and 0 <= col < 10):
            print("Coordinates out of board range.\n")
            continue

        if board[row][col] != '.':
            print("This field has already been revealed.\n")
            continue

        move_count += 1

        if (row, col) in ships:
            board[row][col] = 'X'
            hits.add((row, col))
            print("Hit!\n")
        else:
            board[row][col] = 'O'
            print("Try again.\n")

    print_board(board)
    print(f"Game over! You sank all the ships in {move_count} moves.")

game()
