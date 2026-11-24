"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt.
The joke is a single sentence, well under the 200 character cap.
"""

from pathlib import Path

JOKE = "I asked my wife why she keeps a ladder in the kitchen, and she said it's for when the steaks are high."

OUTPUT_PATH = Path("/output/entry.txt")


MAX_CHARS = 200


def main() -> None:
    joke = JOKE.strip()
    if not joke or len(joke) > MAX_CHARS:
        raise ValueError("joke must be 1 to 200 characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(joke, encoding="utf-8")


if __name__ == "__main__":
    main()
