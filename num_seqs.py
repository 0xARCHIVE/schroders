"""Calculate the number of valid keypad sequences of the specified length."""

import argparse

from keypad import build_keypad_from_csv

if __name__ == "__main__":
    # parse args
    parser = argparse.ArgumentParser(
        description="Calculate the number of valid keypad"
        " sequences of the specified length."
    )
    parser.add_argument(
        "--layout",
        dest="layout_csv",
        type=str,
        required=True,
        help="Keypad layout CSV file",
    )
    parser.add_argument(
        "--length",
        dest="seq_length",
        type=int,
        required=True,
        help="Sequence length",
    )
    args = parser.parse_args()

    # process layout CSV
    keypad = build_keypad_from_csv(args.layout_csv)

    # calculate number of sequences
    valid_seqs = keypad.generate_seqs(length=args.seq_length)
    num_seqs = len(valid_seqs)

    print(num_seqs)
