#!/usr/bin/env python3
"""Say What Actually Broke — one line of honest error copy.

Writes a single line of software error copy to /output/entry.txt.
The line names a real failure (a full disk) in plain words, says what
to do next, and carries one joke a reader can repeat out loud.

Deterministic: no randomness, no timestamps, no network, no input.
Python standard library only.
"""

import os
import sys

ENTRY_LINE = (
    "The disk is full, so your file is waiting outside in the rain "
    "with its suitcase. Free some space and let it back in."
)


def main() -> int:
    output_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY_LINE + "\n")
    print(ENTRY_LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
