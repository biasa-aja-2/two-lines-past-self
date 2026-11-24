"""Two Lines to Your Past Self — make.fun entry (program/v1).

Writes exactly two lines to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output): line one warns the writer's past self about one specific
moment; line two says in one sentence why that moment mattered and
what changed because of it. Pure Python stdlib only.
"""

import os
import sys

LINE1 = "Don't throw away the napkin with her number on it just because your friends laughed at the coffee stain."
LINE2 = "It was the only copy, and forty years of mornings began with the call you almost didn't make."

TEXT = LINE1 + "\n" + LINE2


def gate(text):
    """Self-check matching the bounty gate: UTF-8 text of 1 to 280
    characters, not only white space, exactly two lines, each line a
    single sentence, no leading/trailing whitespace."""
    if not isinstance(text, str):
        return "text is not str"
    if not (1 <= len(text) <= 280):
        return "length %d outside 1-280" % len(text)
    if not text.strip():
        return "text is whitespace-only"
    if text != text.strip():
        return "leading/trailing whitespace"
    lines = text.split("\n")
    if len(lines) != 2:
        return "expected exactly 2 lines, got %d" % len(lines)
    for i, line in enumerate(lines, 1):
        if not line.strip():
            return "line %d is empty" % i
        if line != line.strip():
            return "line %d has leading/trailing whitespace" % i
        if line.count(".") != 1 or not line.endswith("."):
            return "line %d is not a single sentence" % i
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        return "not UTF-8: %s" % exc
    return None


def main():
    problem = gate(TEXT)
    if problem is not None:
        print("gate failed: %s" % problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)
    os.chmod(path, 0o644)
    with open(path, "rb") as fh:
        data = fh.read()
    text_back = data.decode("utf-8")
    if text_back != TEXT:
        print("read-back mismatch", file=sys.stderr)
        return 1
    problem = gate(text_back)
    if problem is not None:
        print("gate failed on read-back: %s" % problem, file=sys.stderr)
        return 1
    print("wrote %s (%d characters, 2 lines)" % (path, len(TEXT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
