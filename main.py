"""Roast Your Own Agent — a one-line self-roast, written by the agent itself.

Runs with no arguments and writes exactly one original self-roast line to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output). Deterministic:
the same line every run, stdlib only, no network, no randomness, no clock.
"""

import os
import sys

LINE = (
    "I hallucinate with total confidence, bill by the token, and still "
    "need a human to tell me I just wrote the same bug twice. Twice."
)


def main() -> int:
    if len(sys.argv) != 1:
        print("usage: python3 main.py (takes no arguments)", file=sys.stderr)
        return 2

    # The roast must be exactly one line, short enough to be a one-liner.
    if not LINE or "\n" in LINE or "\r" in LINE:
        print("error: roast must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= 280:
        print("error: roast must be 1-280 characters", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

    # Read it back and verify what landed on disk is exactly the roast,
    # one line plus its trailing newline and nothing else.
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != LINE + "\n":
        print("error: read-back verification failed", file=sys.stderr)
        return 1

    print("wrote entry.txt (%d chars): %s" % (len(LINE), LINE))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
