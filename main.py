#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message — make.fun entry.

Writes a single one-line commit message (82 characters) to /output/entry.txt.
The line stacks four beats on one fix: the login bug is "fixed" by logging
everyone in as admin, and the engineer proudly reports both numbers — support
tickets down 100%, admins up 100%. The disaster is stated as a win.

Revision history: v1 ended on "support tickets down 100%" alone, which left
the reader to infer why tickets vanished. A head-to-head duel against five
challenger lines showed the explicit closing beat lands harder, so v2 pairs
the success metric with the disaster metric in parallel — the irony is now
stated in the line itself instead of implied.
"""
import os

ENTRY = "fix: login bug by logging everyone in as admin — tickets down 100%, admins up 100%"

def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
