#!/usr/bin/env python3
"""Dad Joke Showdown — one dad joke, written to the output file.

Pure Python standard library only. The joke is the whole entry:
a father, a ladder, a barbecue, and a pun that does double duty.
"""

import os

JOKE = (
    "I asked Dad why he brought a ladder to the barbecue. He said, "
    "'The steaks have never been higher.'"
)


def main():
    if not 1 <= len(JOKE) <= 200:
        raise SystemExit("joke must be 1-200 characters, got %d" % len(JOKE))
    if JOKE != JOKE.strip():
        raise SystemExit("joke must not start or end with whitespace")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, "entry.txt")
    data = JOKE.encode("utf-8")
    with open(out, "wb") as f:
        f.write(data)
    print("chars=%d bytes=%d" % (len(JOKE), len(data)))
    print("wrote %s" % out)


if __name__ == "__main__":
    main()
