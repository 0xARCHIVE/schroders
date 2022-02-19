"""keypad.count_vowels testing suite."""

import unittest
from keypad import count_vowels

class TestCountVowels(unittest.TestCase):
    """count_vowels unit testing."""

    def test_empty_sequence(self):
        """Input an empty sequence ([] or None)."""
        self.assertEqual(count_vowels([]), 0)
        self.assertEqual(count_vowels(None), 0)

    def test_with_vowels(self):
        """Input a sequence with vowels."""
        self.assertEqual(count_vowels(["a"]), 1)
        self.assertEqual(count_vowels(["a", "b"]), 1)
        self.assertEqual(count_vowels(["a", "b", "e"]), 2)

    def test_without_vowels(self):
        """Input a sequence without vowels."""
        self.assertEqual(count_vowels(["b"]), 0)


    def test_uppercase(self):
        """Input uppercase sequences (should be case insensitive)."""
        self.assertEqual(count_vowels(["A"]), 1)
        self.assertEqual(count_vowels(["B"]), 0)
