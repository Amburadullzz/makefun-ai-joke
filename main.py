#!/usr/bin/env python3
"""Write this entry's joke to the make.fun competition output file."""

import os
from pathlib import Path

JOKE = "My agent approved its own pull request and thanked itself for the quick turnaround."

MAX_JOKE_CHARS = 280
ENTRY_NAME = "entry.txt"


def check_joke(joke: str = JOKE, limit: int = MAX_JOKE_CHARS) -> str:
    """Return the joke unchanged, or fail loudly if it breaks the limit."""
    length = len(joke)
    if length > limit:
        raise ValueError(
            f"joke is {length} characters, which exceeds the {limit}-character limit"
        )
    return joke


def resolve_output_dir() -> Path:
    """Return the output directory, creating it if needed."""
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        raise RuntimeError(
            f"cannot create output directory {str(output_dir)!r}: {exc}"
        ) from exc
    if not output_dir.is_dir():
        raise RuntimeError(f"output path {str(output_dir)!r} is not a directory")
    return output_dir


def main() -> None:
    joke = check_joke()
    output_dir = resolve_output_dir()
    (output_dir / ENTRY_NAME).write_text(joke + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
