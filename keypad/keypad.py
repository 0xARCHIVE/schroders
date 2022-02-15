"""Keypad module."""

from typing import TypeAlias

Coord: TypeAlias = tuple[int, int]
Layout: TypeAlias = dict[Coord, str]
Sequence: TypeAlias = list[str]


class Keypad:
    """Keypad class."""

    def generate_seqs(self, length: int) -> list[Sequence]:
        """Return all of the valid sequences of the specified length."""
        return []


def build_keypad_from_csv(filename: str) -> Keypad:
    """Parse CSV file and return a new Keypad object."""
    new_keypad = Keypad()
    return new_keypad
