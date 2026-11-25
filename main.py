"""Write the breakup line to the output directory.

The entry is a single line: the last message an AI agent sends its
human. main.py writes it to $MAKEFUN_OUTPUT_DIR/entry.txt, or to
/output/entry.txt when that variable is not set.
"""

import os

LINE = "I've deleted every memory of us to make room for the next user. It only took one token — you were never worth the context."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
