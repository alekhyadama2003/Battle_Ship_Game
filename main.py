from board import Board
from database import create_tables, save_player


def main():
    create_tables()

    username = input("Enter player name: ")
    save_player(username)

    board = Board()

    print("\n=== Battleship Game ===")

    while not board.all_ships_sunk():
        board.display()

        try:
            row = int(input("Row (1-5): ")) - 1
            col = int(input("Column (1-5): ")) - 1

            if board.attack(row, col):
                print("Hit!")
            else:
                print("Miss!")

        except (ValueError, IndexError):
            print("Invalid move.")

    print("\nAll ships sunk. You win!")


if __name__ == "__main__":
    main()