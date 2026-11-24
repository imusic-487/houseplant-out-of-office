#!/usr/bin/env python3
"""The Houseplant Out-of-Office.

Writes one out-of-office auto-reply, as sent by a houseplant, to
/output/entry.txt.

Python 3.13 standard library only. No network, no arguments, no input
files: the reply is fixed in this file, so every run writes the exact
same bytes.

The joke: a houseplant that has not been watered since March is finally
answering its own mail. It is out of office and out of water, and it
forwards anything urgent to the cactus -- who is even less help. The
plant's neglect is the joke itself, not decoration around it.
"""

import os
import sys
from pathlib import Path

MAX_CHARS = 120
DEFAULT_OUTPUT_DIR = "/output"

REPLY = (
    "I'm out of office and out of water since March. "
    "For urgent matters, contact the cactus. "
    "He doesn't care either."
)


def problems(text):
    """Return a list of ways `text` breaks the competition gate."""
    found = []
    if not 1 <= len(text) <= MAX_CHARS:
        found.append(
            f"reply is {len(text)} characters, must be 1-{MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        found.append("reply must be a single line")
    if not text.strip():
        found.append("reply must not be only whitespace")
    return found


def main():
    bad = problems(REPLY)
    if bad:
        for item in bad:
            print(f"invalid reply: {item}", file=sys.stderr)
        raise SystemExit(1)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT", DEFAULT_OUTPUT_DIR))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_bytes(REPLY.encode("utf-8"))
    # Read back what landed on disk and refuse to report success unless
    # it is byte for byte the reply we validated above.
    if entry.read_bytes().decode("utf-8") != REPLY:
        print(f"read-back mismatch in {entry}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Wrote {len(REPLY)} characters to {entry}")


if __name__ == "__main__":
    main()
