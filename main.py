"""Writes one original relaxing text to entry.txt.

Entry for make.fun's "Make the AI judge feel awe" bounty: an old boatman
rowing home on a slow river at dusk, lantern light on the water, the river
carrying the day away while the first stars come out over the far bank.
Python 3.13 standard library only; no network.
"""
import os

TEXT = (
    "The old boatman rows home as the light goes, his lantern swinging low over "
    "the river, and the water takes the day away in small gold pieces. On the far "
    "bank the first stars come out, one by one, and the river keeps them, and keeps "
    "going, and there is nowhere else to be."
)


def main():
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError("entry text must be 1-280 non-whitespace characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
