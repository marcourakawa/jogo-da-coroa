import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from board import Board
import unittest


class TestBoard(unittest.TestCase):
    def test_initial_positions(self):
        board = Board()
        self.assertEqual(board.positions, [" "] * 9)

    def test_make_move(self):
        board = Board()
        result = board.make_move(0, "X")
        self.assertTrue(result)
        self.assertEqual(board.positions[0], "X")

    def test_make_move_invalid(self):
        board = Board()
        board.make_move(0, "X")
        result = board.make_move(0, "O")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
