"""Keypad module."""

import csv
from typing import TypeAlias

Sequence: TypeAlias = list[str]
Coord: TypeAlias = tuple[int, int]
Keypad: TypeAlias = dict[Coord, str]


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
