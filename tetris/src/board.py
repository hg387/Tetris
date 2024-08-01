"""Board module for representing tetris board"""


class InvalidBoardException(Exception):
    """Class representing Board Exceptions"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Board:
    """Board class to represent tetris board"""

    def __init__(self, rows, columns):
        if rows <= 0 or columns <= 0:
            raise InvalidBoardException(
                f"Invalid rows:{rows} or columns:{columns} passed in Board()"
            )

        self._rows = rows
        self._columns = columns
        self._grid = [[0 for _ in range(columns)] for _ in range(rows)]

    @property
    def grid(self):
        """
        getter to get grid of the board

            Return:
                grid (List[List[int]])
        """
        return self._grid

    @property
    def size(self):
        """
        getter to get size of the board

            Return:
                (int, int) -> (number of rows, number of columns)
        """
        return (self._rows, self._columns)
