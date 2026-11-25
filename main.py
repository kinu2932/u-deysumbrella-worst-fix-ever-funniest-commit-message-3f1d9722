#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message — make.fun entry.

Writes a single one-line commit message (74 characters) to /output/entry.txt.
The line stacks three punchlines on one fix: the login bug is "fixed" by
logging everyone in as admin, and the engineer brags that support tickets
are down 100% — the metric improved because the fix broke auth for everyone.
"""
import os

ENTRY = "fix: login bug by logging everyone in as admin — support tickets down 100%"

def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
