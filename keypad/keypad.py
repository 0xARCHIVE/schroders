"""Keypad module."""

import csv
from typing import TypeAlias

Sequence: TypeAlias = list[str]
Coord: TypeAlias = tuple[int, int]
Keypad: TypeAlias = dict[Coord, str]


def count_vowels(seq: Sequence) -> int:
    """Return the number of vowels in seq."""
    if not seq:
        return 0

    vowels = ["a", "e", "i", "o", "u"]

    count = 0
    for val in seq:
        if val.lower() in vowels:
            count += 1
    return count


def generate_seqs(keypad: Keypad, length: int) -> list[Sequence]:
    """Return all of the valid sequences of the specified length."""
    return []


def build_keypad_from_csv(filename: str) -> Keypad:
    """Parse CSV file and return a new Keypad object."""
    new_keypad = {}

    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            x, y, value = row
            coord: Coord = (int(x), int(y))
            new_keypad[coord] = value

    return new_keypad
