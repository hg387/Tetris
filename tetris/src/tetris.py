"""Module for Tetris in optimized way"""

#!/usr/bin/env python3
import sys
from .utils import create_pieces, create_board, read_games


class TetrisInputException(Exception):
    """Class representing Tetris Exceptions"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Tetris:
    """Class representing Tetris"""

    pieces = create_pieces()

    def __init__(self, rows, cols, piece_size=4):
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

    def find_complete_rows(self):
        """
        Find all the completed rows to remove in current tetris board

                Returns:
                        completed_rows (List[int]): list of completed rows indices
        """
        completed_rows = []

        for row in range(self.rows - 1, -1, -1):
            row_sum = sum(self.board.grid[row])
            if row_sum == self.cols:
                completed_rows.append(row)

        return completed_rows

    def remove_n_shift_row(self, row_num, end_num=0, removed_rows=0):
        """
        Remove a completed row and shift all the rows above the completed row

                Parameters:
                        row_num (int): row to be removed
                        end_num (int): next completed row
                        removed_rows (int): number of removed completed rows
        """
        if (
            row_num < 0
            or row_num >= self.rows
            or end_num < 0
            or end_num >= self.rows
        ):
            return

        self.board.grid[row_num] = [0 for _ in range(self.cols)]
        for row in range(row_num, end_num, -1):
            for col in range(self.cols):
                self.board.grid[row + removed_rows][col] = self.board.grid[
                    row - 1
                ][col]
                self.board.grid[row - 1][col] = 0

    def remove_n_shift_rows(self, completed_rows):
        """
        Remove all the completed rows and shift rows

                Parameters:
                        completed_rows (List[int]): list of completed rows indices
        """
        nums_completed_rows = len(completed_rows)

        for num_row in range(nums_completed_rows):
            if num_row != nums_completed_rows - 1:
                self.remove_n_shift_row(
                    completed_rows[num_row],
                    completed_rows[num_row + 1],
                    num_row,
                )
            else:
                self.remove_n_shift_row(completed_rows[num_row], 0, num_row)

    def handle_move(self, inp):
        """
        Wrapper function to insert a piece, remove completed rows,
        and shift rows

            Parameters:
                        inp (string): Piece and start index such as Q8
        """
        self.insert_piece(inp)

        completed_rows = self.find_complete_rows()
        self.remove_n_shift_rows(completed_rows)

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
        tetris = Tetris(100, 10)
        moves_breakdown = moves.split(",")

        for move in moves_breakdown:
            tetris.handle_move(move.strip())

        print(tetris.calculate_heights())
