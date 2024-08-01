import time
from unittest import TestCase
from pathlib import Path
from src.tetris_naive import TetrisNaive
from src.tetris import Tetris


class TestTetris(TestCase):

    def test_tetris_input_file(self):
        start_time = time.time()
        actual = []
        expected = [
            2,
            4,
            0,
            2,
            4,
            1,
            0,
            2,
            2,
            2,
            1,
            1,
            4,
            3,
            1,
            2,
            1,
            8,
            8,
            0,
            3,
        ]
        file_path = "test_input.txt"
        with open(
            (Path(__file__).parent / file_path).absolute(), "r"
        ) as reader:
            for line in reader.readlines():
                line = line.rstrip("\n")
                tetris = Tetris(100, 10)

                moves = line.split(",")
                for move in moves:
                    move = move.strip()
                    tetris.handle_move(move)

                actual.append(tetris.calculate_heights())
                print(f"For inp: {line} height is {actual[-1]}")

        end_time = time.time()
        print(
            f"Execution time for test_tetris_input_file is {end_time - start_time}"
        )
        assert all([a == b for a, b in zip(actual, expected)])

    def test_tetris_naive_input_file(self):
        start_time = time.time()
        actual = []
        expected = [
            2,
            4,
            0,
            2,
            4,
            1,
            0,
            2,
            2,
            2,
            1,
            1,
            4,
            3,
            1,
            2,
            1,
            8,
            8,
            0,
            3,
        ]
        file_path = "test_input.txt"
        with open(
            (Path(__file__).parent / file_path).absolute(), "r"
        ) as reader:
            for line in reader.readlines():
                line = line.rstrip("\n")
                tetris = TetrisNaive(100, 10)

                moves = line.split(",")
                for move in moves:
                    move = move.strip()
                    tetris.handle_move(move)

                actual.append(tetris.calculate_heights())
                print(f"For inp: {line} height is {actual[-1]}")

        end_time = time.time()
        print(
            f"Execution time for test_tetris_naive_input_file is {end_time - start_time}"
        )
        assert all([a == b for a, b in zip(actual, expected)])
