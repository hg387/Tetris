"""Utils for Tetris"""

import sys
from .piece import Piece
from .board import Board


def read_games():
    """
    Function to read games from stdin

        Return:
            games (List[string]): List of games as a string
    """
    games = []
    for line in sys.stdin:
        line = line.rstrip("\n").strip()
        games.append(line)

    return games


def create_board(rows, columns):
    """
    Function to create tetris board
        Parameters:
            rows (int): number of rows
            columns (int): number of columns

        Return:
            Board: board of size rows and columns
    """
    return Board(rows, columns)


def create_pieces():
    """
    Function to create tetris by default

        Return:
            pieces (Dict[string, Piece]): map of pieces as string -> Piece
    """
    pieces = {}
    Q = Piece(4, min_cols_size=2)
    Q.edit_row(0, [0, 0, 0, 0])
    Q.edit_row(1, [0, 0, 0, 0])
    Q.edit_row(2, [2, 2, 0, 0])
    Q.edit_row(3, [2, 2, 0, 0])
    pieces["Q"] = Q

    T = Piece(4, min_cols_size=3)
    T.edit_row(0, [0, 0, 0, 0])
    T.edit_row(1, [0, 0, 0, 0])
    T.edit_row(2, [2, 2, 2, 0])
    T.edit_row(3, [0, 2, 0, 0])
    pieces["T"] = T

    L = Piece(4, min_cols_size=2)
    L.edit_row(0, [0, 0, 0, 0])
    L.edit_row(1, [2, 0, 0, 0])
    L.edit_row(2, [2, 0, 0, 0])
    L.edit_row(3, [2, 2, 0, 0])
    pieces["L"] = L

    Z = Piece(4, min_cols_size=3)
    Z.edit_row(0, [0, 0, 0, 0])
    Z.edit_row(1, [0, 0, 0, 0])
    Z.edit_row(2, [2, 2, 0, 0])
    Z.edit_row(3, [0, 2, 2, 0])
    pieces["Z"] = Z

    S = Piece(4, min_cols_size=3)
    S.edit_row(0, [0, 0, 0, 0])
    S.edit_row(1, [0, 0, 0, 0])
    S.edit_row(2, [0, 2, 2, 0])
    S.edit_row(3, [2, 2, 0, 0])
    pieces["S"] = S

    I = Piece(4, min_cols_size=4)
    I.edit_row(0, [0, 0, 0, 0])
    I.edit_row(1, [0, 0, 0, 0])
    I.edit_row(2, [0, 0, 0, 0])
    I.edit_row(3, [2, 2, 2, 2])
    pieces["I"] = I

    J = Piece(4, min_cols_size=2)
    J.edit_row(0, [0, 0, 0, 0])
    J.edit_row(1, [0, 2, 0, 0])
    J.edit_row(2, [0, 2, 0, 0])
    J.edit_row(3, [2, 2, 0, 0])
    pieces["J"] = J

    return pieces
