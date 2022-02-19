"""keypad.get_knight_moves testing suite."""

import unittest

from keypad import get_knight_moves


class TestGetKnightMoves(unittest.TestCase):
    """get_knight_moves unit testing."""

    def test_invalid_start_coord(self):
        """Input a start_coord not in the keypad."""
        keypad = {}
        start_coord = (0, 0)

        self.assertEqual(get_knight_moves(keypad, start_coord), set())

    def test_valid_start_coord(self):
        """Input start_coord within the keypad."""
        keypad = {(0, 0)}
        start_coord = (0, 0)

        self.assertEqual(get_knight_moves(keypad, start_coord), set())

    def test_valid_moves(self):
        """Input a start_coord with moves within the keypad."""
        keypad = {
            (0, 0),
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (-1, 2),
            (1, -2),
            (-1, -2),
        }
        start_coord = (0, 0)
        expected = {
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (-1, 2),
            (1, -2),
            (-1, -2),
        }

        self.assertEqual(get_knight_moves(keypad, start_coord), expected)
