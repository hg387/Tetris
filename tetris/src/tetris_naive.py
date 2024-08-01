"""Module for Tetris in naive way"""

#!/usr/bin/env python3
import sys
from .utils import create_pieces, create_board, read_games


class TetrisInputException(Exception):
    """Class representing Tetris Exceptions"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class TetrisNaive:
    """Class representing Tetris"""

    pieces = create_pieces()

    def __init__(self, rows, cols, piece_size=4):
        self.count = 0
        self.rows = rows + piece_size
        self.cols = cols
        self.piece_size = piece_size
        self.board = create_board(self.rows, self.cols)

    def insert_piece(self, inp):
        """
        Insert a given piece in the tetris board

                Parameters:
                        inp (string): Piece and start index such as Q8
        """
        try:
            piece = self.pieces[inp[0]]
            start_index = int(inp[1:])
            end_index = start_index + piece.min_cols_size
        except Exception as err:
            raise TetrisInputException(
                f"Invalid input found for a piece {inp}!!"
            ) from err

        if end_index > self.cols:
            raise TetrisInputException(
                f"Invalid input found for a piece {inp}!!"
            )

        for row in range(self.piece_size):
            for col in range(start_index, end_index):
                self.board.grid[row][col] = piece.block[row][col - start_index]

        lowest_distance = sys.maxsize
        for col in range(start_index, end_index):
            lowest_row = self.rows - 1
            for row in range(self.rows - 1, -1, -1):
                if self.board.grid[row][col] == 1:
                    lowest_row = row - 1
                elif self.board.grid[row][col] == 2:
                    lowest_distance = min(lowest_distance, lowest_row - row)
                    lowest_row -= 1

        if lowest_distance != sys.maxsize:
            for row in range(self.piece_size):
                for col in range(start_index, end_index):
                    if self.board.grid[row][col] == 2:
                        self.board.grid[row][col] = 0
                        self.board.grid[row + lowest_distance][col] = 1

    def find_complete_row(self):
        """
        Find all the completed rows to remove in current tetris board

                Returns:
                        row_num (int): row index of completed row
        """
        row_num = -1
        for row in range(self.rows - 1, -1, -1):
            row_sum = sum(self.board.grid[row])
            if row_sum == self.cols:
                return row

        return row_num

    def remove_n_shift_row(self, row_num):
        """
        Remove a completed row and shift all the rows above the completed row

                Parameters:
                        row_num (int): row to be removed
        """
        if row_num < 0 or row_num >= self.rows:
            return

        for row in range(row_num, 0, -1):
            for col in range(self.cols):
                self.board.grid[row][col] = self.board.grid[row - 1][col]
                self.board.grid[row - 1][col] = 0

    def handle_move(self, inp):
        """
        Wrapper function to insert a piece, remove completed rows,
        and shift rows

            Parameters:
                        inp (string): Piece and start index such as Q8
        """
        self.insert_piece(inp)

        row_num = self.find_complete_row()

        while row_num != -1:
            self.remove_n_shift_row(row_num)
            row_num = self.find_complete_row()
            self.count += 1

    def calculate_heights(self):
        """
        Calculate maximum height of the board after iterating over board
        """
        max_height = 0

        for col in range(self.cols):
            for row in range(self.rows - 1, -1, -1):
                if self.board.grid[row][col] == 1:
                    max_height = max(max_height, self.rows - row)

        return max_height


if __name__ == "__main__":
    try:
        games = read_games()
    except Exception as error:
        raise TetrisInputException("Error while parsing the stdin!!") from error

    for moves in games:
        tetris = TetrisNaive(100, 10)
        moves_breakdown = moves.split(",")

        for move in moves_breakdown:
            tetris.handle_move(move.strip())

        print(tetris.calculate_heights())
