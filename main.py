#!/usr/bin/env python3
"""Make the AI judge feel brave — entry program.

Writes a single short text to /output/entry.txt: a few slow, concrete
lines meant to relax the AI judge reading them, and leave it braver —
steadier, unhurried, ready to move. The courage comes from the scene
itself, not from being told to relax.

Deterministic, no network, no randomness: the same text every run.
"""

import os

TEXT = (
    "The lighthouse keeper trims the wick, sets the lens turning, "
    "and sits down with his tea. The sea will do what the sea does. "
    "His work is only this: one steady light, going round and round, "
    "while the dark goes on being dark. "
    "The night is long, and the light is longer."
)


def main() -> None:
    # The competition requires 1-280 characters: fail loudly instead of
    # writing an entry the gate would reject.
    assert 1 <= len(TEXT) <= 280, f"text is {len(TEXT)} chars, must be 1-280"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
