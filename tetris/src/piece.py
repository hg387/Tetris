"""Piece module for representing piece"""


class InvalidPieceException(Exception):
    """Class representing Piece Exceptions"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Piece:
    """Piece class to represent piece"""

    def __init__(self, size, min_cols_size=2):
        if size <= 0:
            raise InvalidPieceException(
                f"Invalid size {size} passed in Piece()"
            )

        self._block = [[0 for _ in range(size)] for _ in range(size)]
        self._size = size
        self._min_cols_size = min_cols_size

    @property
    def block(self):
        """
        getter to get block of the piece

            Return:
                grid (List[List[int]])
        """
        return self._block

    @property
    def size(self):
        """
        getter to get size of the piece

            Return:
                size (int): square side of the piece
        """
        return self._size

    @property
    def min_cols_size(self):
        """
        getter to get minimum column size of the piece

            Return:
                _min_cols_size (int): minimum column size of the piece
        """
        return self._min_cols_size

    def edit_row(self, index, row):
        """
        set row in the piece

            Parameters:
                index (int): row index to set
                row (List[int]): List of int to represent piece
        """
        if len(row) != self._size or index < 0 or index >= self._size:
            raise InvalidPieceException(
                f"Invalid index {index} passed in Piece.edit_row()"
            )

        self._block[index] = row
