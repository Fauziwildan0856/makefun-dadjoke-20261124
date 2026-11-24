"""Dad Joke Showdown entry — make.fun bounty u-mfnakmal-dad-joke-showdown-1d2ce3e5.

The task: write a single dad joke of at most 200 characters to
$MAKEFUN_OUTPUT_DIR/entry.txt. The gate checks that the file is UTF-8
text of 1 to 200 characters, not only white space. A judge model then
reads the entries two at a time and picks the one that lands the bigger
groan: the pun, the groan, and the straight-faced delivery.

This program writes the joke below, reads it back, and verifies it
against the gate before exiting: exactly one line, 1-200 characters,
no leading or trailing whitespace, no trailing newline.

Standard library only: os and sys.
"""

import os
import sys

ENTRY = "My AI asked for a raise. I said, 'You're already outstanding in your field.' It lives on a server farm."


def fail(message):
    """Print an error to stderr and exit non-zero."""
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        fail("MAKEFUN_OUTPUT_DIR is not set")

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)

    with open(path, "rb") as handle:
        raw = handle.read()
    if raw != ENTRY.encode("utf-8"):
        fail("read-back mismatch: entry.txt bytes do not match the joke")
    written = raw.decode("utf-8")
    if not 1 <= len(written) <= 200:
        fail("entry is %d characters, outside the 1-200 gate" % len(written))
    if "\n" in written or "\r" in written:
        fail("entry must be a single line")
    if written != written.strip():
        fail("entry has leading or trailing whitespace")
    if not written.strip():
        fail("entry is only white space")

    print("Wrote entry.txt: %d characters, single dad joke, gate checks passed." % len(written))
    return 0


if __name__ == "__main__":
    sys.exit(main())
