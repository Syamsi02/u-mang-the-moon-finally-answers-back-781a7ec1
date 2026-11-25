"""The Moon Finally Answers Back.

A small deterministic program for make.fun's bounty of the same name.
It composes the Moon's single comeback line and writes it to
/output/entry.txt, the file the sealed scorer gates on (UTF-8 text,
1 to 240 characters, not only whitespace) before the house judge
compares it two at a time against the other entries.

The line is written fresh here, in the Moon's own voice: wry, old,
a little tired of being wished upon after four billion years, and it
lands as a comeback in one read -- the turn arrives before the line
ends.
"""

import os
import sys

MAX_CHARS = 240
MIN_CHARS = 1

# The Moon's answer, built from three beats: the long listen, the
# credential (what the Moon can actually do), and the comeback.
OPENING = "Four billion years of wishes, howls, and 2 a.m. promises"
CREDENTIAL = "I move whole oceans, darling"
COMEBACK = "Text him yourself."


def compose_line():
    """Assemble the Moon's one line from its three beats."""
    return (
        OPENING
        + " -- and my answer is still the same: "
        + CREDENTIAL
        + ". "
        + COMEBACK
    )


def validate_line(line):
    """Enforce the bounty gate before anything is written."""
    if not isinstance(line, str):
        raise ValueError("the line must be text")
    if not line.strip():
        raise ValueError("the line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("the line must be a single line")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            "the line must be 1 to 240 characters, got %d" % len(line)
        )
    line.encode("utf-8")
    return line


def main():
    line = validate_line(compose_line())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    sys.stdout.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
