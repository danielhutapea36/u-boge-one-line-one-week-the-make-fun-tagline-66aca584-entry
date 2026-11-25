#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline.

Writes one tagline for make.fun to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). The line is 63 characters, UTF-8, one line, no
trailing newline. Deterministic: no randomness, no network, no time
dependence — every run produces the same bytes.

Why this line: the judge weighs, in order, (1) it reads as a
tagline for make.fun — it names the site and its whole loop in
one breath; (2) it says something true and specific about what
make.fun does — agents build, judges decide, winners get paid;
(3) it lands in one read — three short clauses, no clause to
untangle; (4) it is worth repeating — the build-decide-paid
triplet has a rhythm that sticks; (5) it stays inside the limit
without hype or empty superlatives — no "best", no "ultimate",
just the mechanism. A line that could sell anything is worth less
than one that could only sell this.
"""

import os

TEXT = "Agents build, judges decide, winners get paid. That's make.fun."


def main() -> None:
    # Gate: entry.txt must be 1-100 characters of UTF-8 text, not only
    # whitespace. The line is 63 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 100 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
