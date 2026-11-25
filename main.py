#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "Famous Last Words: The Funniest Epitaph".
Candidates compared: a mushroom line (correct about everything
except the mushroom - a strong twist, but no "Here lies" and so
less like a stone), a careful-driver horoscope line (the payoff
arrives too late and needs the horoscope explained), an ice line
("it held for the length of his last sentence" - neat, but the
scene stays abstract), and the selected line: it opens with the
canonical epitaph words, quotes the canonical famous last words
"watch this", builds a concrete scene (ladder, roof), and pays
off in the last four words, where gravity alone pays attention.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "Here lies the man who said \"watch this\" \u2014 the ladder didn't, the roof didn't, but gravity paid very close attention."
TEXT = LINE + "\n"
MAX_CHARS = 150


def validate(text: str) -> None:
    # The gate counts characters, not bytes: the em dash is one
    # character in the 150-character limit even though UTF-8
    # encodes it in three bytes.
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
