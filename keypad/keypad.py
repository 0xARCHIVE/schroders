"""Keypad module."""

import csv
from typing import TypeAlias

Coord: TypeAlias = tuple[int, int]
Sequence: TypeAlias = list[str]
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


def get_knight_moves(keypad: Keypad, start_coord: Coord) -> set[Coord]:
    """Return all coords that are a knight move away from start_coord."""
    if start_coord not in keypad:
        return set()

    x, y = start_coord
    possible_moves = {
        (x + 2, y + 1),
        (x + 2, y - 1),
        (x - 2, y + 1),
        (x - 2, y - 1),
        (x + 1, y + 2),
        (x - 1, y + 2),
        (x + 1, y - 2),
        (x - 1, y - 2),
    }

    return {coord for coord in possible_moves if coord in keypad}


def generate_seqs_from(
    keypad: Keypad, start_coord: Coord, length: int
) -> list[Sequence]:
    """Return all coord sequences of the length starting from start_coord."""
    if length == 1:
        return [[keypad[start_coord]]]  # a list one 1-length sequence
    else:
        next_moves = get_knight_moves(keypad, start_coord)

        sub_sequences = [
            sequence
            for next_move in next_moves
            for sequence in generate_seqs_from(keypad, next_move, length - 1)
        ]

        return [
            generate_seqs_from(keypad, start_coord, 1)[0] + sequence
            for sequence in sub_sequences
        ]


def generate_seqs(
    keypad: Keypad, length: int, max_vowels: int
) -> list[Sequence]:
    """Return all of the valid sequences of the specified length."""
    sequences = []

    for coord, val in keypad.items():
        for sequence in generate_seqs_from(keypad, coord, length):
            # check for number of vowels
            if count_vowels(sequence) <= max_vowels:
                sequences.append(sequence)

    return sequences


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
