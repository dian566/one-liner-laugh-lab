#!/usr/bin/env python3
"""One-liner joke entry for make.fun: the sock started it."""

# The text below is fixed by the bounty brief; this program only writes it out.

from os import makedirs

TEXT = (
    "The sock attacked first — "
    "I merely performed a hostile ingestion in self-defense."
)


def write_entry() -> None:
    """Write the funny line to /output/entry.txt, nothing else."""
    if len(TEXT) > 200 or not TEXT.strip():
        raise ValueError("entry must be a non-empty line of at most 200 characters")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)


if __name__ == "__main__":  # run as a script
    write_entry()
