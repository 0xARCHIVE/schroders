"""Keypad module."""

from typing import TypeAlias

Sequence: TypeAlias = list[str]


class Keypad:
    """Keypad class."""

    def generate_seqs(self, length: int) -> list[Sequence]:
        """Return all of the valid sequences of the specified length."""
        return []


def build_keypad_from_csv(filename: str) -> Keypad:
    """Parse CSV file and return a new Keypad object."""
    return Keypad()
