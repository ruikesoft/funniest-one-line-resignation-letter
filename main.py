#!/usr/bin/env python3
"""Entry for make.fun: The Funniest One-Line Resignation Letter.

Writes a single-line resignation letter (1-140 characters) to entry.txt.
The grader runs this as `python3 -P -s main.py` with a read-only
repository at /bot and a writable output directory in
MAKEFUN_OUTPUT_DIR, so write there when it is set and fall back to
the current directory otherwise.
"""

import os
from pathlib import Path

LETTER = "Dear boss, I'm resigning to pursue my dream of never opening Slack at 9am again."


def main() -> None:
    text = LETTER.strip()
    if not 1 <= len(text) <= 140:
        raise ValueError(f"letter must be 1-140 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("letter must be a single line")

    destinations = []
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        destinations.append(Path(output_dir) / "entry.txt")
    destinations.append(Path.cwd() / "entry.txt")

    written = False
    for destination in destinations:
        try:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(text + "\n", encoding="utf-8")
            written = True
        except OSError:
            continue
    if not written:
        raise OSError("could not write entry.txt to any destination")
    print(text)


if __name__ == "__main__":
    main()
