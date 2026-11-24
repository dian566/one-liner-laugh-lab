"""Entry for the make.fun bounty "One-Liner Laugh Lab".

Writes a single funny line of at most 200 characters and nothing else to /output/entry.txt.
"""

import os

LINE = "The sock attacked first \u2014 I merely performed a hostile ingestion in self-defense."

assert len(LINE) <= 200, "entry must be at most 200 characters"
assert LINE.strip(), "entry must not be empty"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
