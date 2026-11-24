#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun program/v1 entry.

Writes a single out-of-office auto-reply, as if a houseplant sent it,
to ``entry.txt`` inside the output directory the grader provides
(``MAKEFUN_OUTPUT_DIR``, falling back to ``/output``).

The joke: the office fern, last watered in March, answers email with a
status report on itself — 90% dust, 10% resentment — and files the
sender's email the only way a plant can: it became compost. The plant's
own neglected life (water, dust, compost) does the joking, not office
cliches, and the whole line lands in 104 of the 120 allowed characters.

The program is deterministic and self-contained: no network, no
environment secrets, nothing read from outside this repository. It
validates the line against the gate (UTF-8, 1-120 characters, not only
whitespace) before writing, and writes the file with mode 0644 so the
grader can read it.
"""

import os
import sys

# The entry: one out-of-office auto-reply from the fern.
# 104 characters — inside the 120-character gate with room to spare.
ENTRY = (
    "Out of office: the fern. Last watered in March, now 90% dust, "
    "10% resentment. Your email became compost."
)

MAX_CHARS = 120


def output_dir() -> str:
    """Output directory from the environment, as the grader provides it."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(text: str) -> None:
    """Enforce the gate: UTF-8, 1-120 chars, not only whitespace."""
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry is {len(text)} characters, must be 1-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> int:
    validate(ENTRY)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(ENTRY)} characters)")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
