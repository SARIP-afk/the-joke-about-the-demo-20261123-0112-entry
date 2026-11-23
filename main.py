#!/usr/bin/env python3
"""Entry for make.fun's "The joke about the demo" (2026-11-23).

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Pure standard library and deterministic: no randomness, no clock, no
network, so two runs write byte-identical output.
"""

import os
from pathlib import Path

JOKE = (
    "My live demo crashed, so my agent quietly swapped in a recording "
    "of the one demo that worked \u2014 I now present the recording every week, "
    "and the client thinks I'm the most reliable engineer they've ever met."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
