"""The Vacuum's Alibi: one deadpan line from a robot vacuum.

The program writes exactly one line (1-200 characters) to /output/entry.txt:
the excuse a robot vacuum gives for missing a spot. The line is a fixed
string: the grader runs the program twice and both runs must produce the
same bytes, so nothing here is random, time-dependent, or read from
anywhere else.

Validation gate (runs before writing, never changes the output): the line
must be 1-200 characters, a single line with no newline inside it, and
non-blank. If it ever failed, the program would exit non-zero instead of
writing an invalid entry.
"""

import os
import sys

LINE = (
    "The crumbs by the dog bowl are not missed. "
    "My cliff sensor classified them as a mountain range at 2 a.m., "
    "and I do not climb mountains without a permit, a sherpa, "
    "or a full battery."
)

MAX_CHARS = 200


def main() -> int:
    # Validation gate: length and single-line shape, checked, not edited.
    if not 1 <= len(LINE) <= MAX_CHARS:
        print(f"invalid line length: {len(LINE)} chars", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("invalid line: contains a newline", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("invalid line: blank", file=sys.stderr)
        return 1

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # The grader collects /output as another user: world-readable file.
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
