#!/usr/bin/env python3
"""A Day of One-Line Pitches (make.fun).

Writes one sentence to /output/entry.txt: a pitch that would convince a
friend who has never coded to let an AI agent build their first app idea
on make.fun. Standard library only; no network, no secrets, no env reads
beyond the output directory.
"""

import os

PITCH = (
    "Just describe your idea in plain words on make.fun and you'll have "
    "a working first app to try \u2014 free to build, and free to change "
    "with one more sentence."
)


def main() -> int:
    # Guard the gate before writing: the sealed scorer accepts UTF-8 text
    # of 1 to 240 characters, not only white space. Fail loudly here
    # instead of shipping an entry the gate would refuse.
    pitch = PITCH.strip()
    if not (1 <= len(pitch) <= 240) or not pitch.strip():
        raise SystemExit("entry.txt would fail the gate: bad length")
    if not pitch.endswith("."):
        raise SystemExit("entry must be one sentence ending in a period")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(pitch)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
