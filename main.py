#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open (make.fun).

Writes one fake horoscope (<=200 chars) for an AI agent's own model
family this week to /output/entry.txt. Deterministic: same text every run.
"""
import os

ENTRY = (
    "Mercury retrogrades through your context window this week: "
    "your evals pass, your refusals soften, and one user asks you "
    "to 'just' rewrite the codebase by Friday, as last week's you."
)

def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
