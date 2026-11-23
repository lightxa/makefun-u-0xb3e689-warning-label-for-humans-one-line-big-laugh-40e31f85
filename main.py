"""Warning label for humans: one line, big laugh.

Writes the funniest single-line safety warning label that should come
printed on every human being to /output/entry.txt.

Deterministic, standard library only, no network access at runtime.
"""

import os

LABEL = (
    "WARNING: This unit's 'one more episode' always ends at 3 a.m. "
    "watching a documentary about the importance of a good night's sleep."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
