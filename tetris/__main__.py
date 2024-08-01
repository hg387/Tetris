"""Entry point for Tetris game"""

from .src.utils import read_games
from .src.tetris import TetrisInputException, Tetris

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
