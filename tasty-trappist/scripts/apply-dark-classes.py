#!/usr/bin/env python3
"""Idempotent Tailwind dark: class expansion for Astro sources."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "src"


def expand(s: str, util: str, dark: str) -> str:
    """Append dark: variant if util is not already in a dark: context."""
    return re.sub(
        rf"(?<!dark:){re.escape(util)}(?!\s+dark:)",
        f"{util} {dark}",
        s,
    )


def transform(text: str) -> str:
    s = text

    s = expand(s, "bg-white/90", "dark:bg-zinc-950/90")
    s = re.sub(
        r"(?<!dark:)bg-white(?![/])(?!\s+dark:)",
        "bg-white dark:bg-zinc-950",
        s,
    )
    s = expand(s, "bg-zinc-50", "dark:bg-zinc-900")
    # Avoid matching the `bg-zinc-100` inside `hover:bg-zinc-100`
    s = re.sub(
        r"(?<!dark:)(?<!hover:)bg-zinc-100(?!\s+dark:)",
        "bg-zinc-100 dark:bg-zinc-800/70",
        s,
    )
    s = expand(s, "bg-zinc-200/60", "dark:bg-zinc-800/50")

    s = expand(s, "border-zinc-200", "dark:border-zinc-800")
    s = expand(s, "border-zinc-300", "dark:border-zinc-600")
    s = expand(s, "border-zinc-900", "dark:border-zinc-100")

    s = expand(s, "text-zinc-900", "dark:text-zinc-50")
    s = expand(s, "text-zinc-800", "dark:text-zinc-200")
    s = expand(s, "text-zinc-700", "dark:text-zinc-300")
    s = expand(s, "text-zinc-600", "dark:text-zinc-400")
    s = expand(s, "text-zinc-500", "dark:text-zinc-400")
    s = expand(s, "text-zinc-400", "dark:text-zinc-500")
    s = expand(s, "text-black", "dark:text-zinc-50")

    s = expand(s, "hover:bg-zinc-100", "dark:hover:bg-zinc-800")
    s = expand(s, "hover:bg-zinc-50", "dark:hover:bg-zinc-800")
    s = expand(s, "hover:text-zinc-900", "dark:hover:text-zinc-50")
    s = expand(s, "hover:text-zinc-600", "dark:hover:text-zinc-300")
    s = expand(s, "hover:border-zinc-400", "dark:hover:border-zinc-500")

    s = expand(s, "decoration-zinc-300", "dark:decoration-zinc-600")
    s = expand(s, "hover:decoration-zinc-900", "dark:hover:decoration-zinc-300")
    s = expand(s, "hover:decoration-zinc-500", "dark:hover:decoration-zinc-400")

    return s


def main() -> None:
    skip = {"ThemeToggle.astro"}
    for path in sorted(ROOT.rglob("*.astro")):
        if path.name in skip:
            continue
        original = path.read_text(encoding="utf-8")
        updated = transform(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print("updated", path.relative_to(ROOT.parent))


if __name__ == "__main__":
    main()
