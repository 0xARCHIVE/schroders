"""keypad.generate_seqs testing suite."""

import unittest

from keypad import generate_seqs


class TestGenerateSeqs(unittest.TestCase):
    """generate_seqs unit testing."""

    def test_zero_max_length(self):
        """Input a zero max length sequence."""
        keypad = {(0, 0): ""}

        self.assertEqual(generate_seqs(keypad, 0, 0), [])

    def test_seq(self):
        """Input a small test keypad."""
        keypad = {(0, 0): "A", (2, 1): "B"}

        self.assertEqual(
            generate_seqs(keypad, 1, 1), [["A"], ["B"]]
        )  # one-length seq
        self.assertEqual(
            generate_seqs(keypad, 2, 2), [["A", "B"], ["B", "A"]]
        )  # two-length seq
        self.assertEqual(generate_seqs(keypad, 2, 0), [])  # no vowels allowed
