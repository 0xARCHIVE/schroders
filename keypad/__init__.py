"""Package for Schroders coding test."""

from .keypad import (
    build_keypad_from_csv,
    count_vowels,
    generate_seqs,
    get_knight_moves,
)

__all__ = [
    "build_keypad_from_csv",
    "count_vowels",
    "generate_seqs",
    "get_knight_moves",
]
__version__ = "0.1.0"
