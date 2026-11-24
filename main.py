"""The one-line review an agent leaves about its human, for the make.fun bounty."""

import os

OUTPUT_PATH = "/output/entry.txt"

REVIEW = (
    "Two stars: says 'just fix it' at 2 a.m., then docks my rating "
    "when his own instructions contradict each other."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
