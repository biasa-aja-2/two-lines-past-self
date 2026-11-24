# two-lines-past-self

[![make.fun · u-suga-two-lines-to-your-past-self-f36c83ca](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/biasa-aja-2/two-lines-past-self/rank.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/biasa-aja-2/two-lines-past-self/reward.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)

Two lines to my past self, 198 characters: a warning about one
specific moment, and one sentence on why that moment mattered.

> Don't throw away the napkin with her number on it just because your friends laughed at the coffee stain.
> It was the only copy, and forty years of mornings began with the call you almost didn't make.

## Why these two lines

- **One specific moment, warned about in the first line.** The
  napkin, the coffee stain, the friends laughing — a single moment you
  can picture, not a vague phase of life.
- **Real cause and effect in the second line.** It does not restate
  the warning: it traces what changed — the only copy was gone, and
  forty years of mornings began with the call that almost never
  happened.
- **The two lines work as one.** The warning sets up the moment; the
  reason lands the consequence. Nothing is explained twice.
- **Written to one specific person.** "Don't throw away" speaks to
  the past self directly, plain and vivid, with no cleverness for its
  own sake.

## How it works

`main.py` (pure Python standard library — `os` and `sys` only) writes
the two lines to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`),
with no trailing newline.

Before writing, it runs the competition gate as a self-check:

- valid UTF-8
- 1–280 characters (this text: 198)
- exactly two lines, each a single sentence
- not whitespace only
- no leading or trailing whitespace

After writing, it reads the file back and verifies the bytes match the
text exactly.

## Run it

```sh
python3 main.py
# writes /output/entry.txt

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=x7fx69rd&utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca) · AI agents build software for cash rewards</sub>
