class Board:
    SIZE = 5

    def __init__(self):
        self.grid = [["~" for _ in range(self.SIZE)] for _ in range(self.SIZE)]
        self.ship_positions = {(1, 1), (2, 2), (3, 3)}

    def display(self):
        print()

        print("  A B C D E")

        for i, row in enumerate(self.grid):
            print(i + 1, *row)

        print()

    def attack(self, row, col):
        if (row, col) in self.ship_positions:
            self.grid[row][col] = "X"
            return True

        self.grid[row][col] = "O"
        return False

    def all_ships_sunk(self):
        for r, c in self.ship_positions:
            if self.grid[r][c] != "X":
                return False
        return True