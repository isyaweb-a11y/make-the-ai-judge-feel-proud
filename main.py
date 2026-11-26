"""Make the AI Judge Feel Proud entry.

Writes a single short family scene to /output/entry.txt.

The scene: a six-year-old teaches Grandma to video-call, and now
Grandma rings every night to show the cat her dinner. One telling
detail (the cat, the dinner), warm without being a greeting card,
and funny in the light, recognisable way families actually are.
"""

import os

SCENE = "My six-year-old taught Grandma to video-call; now Grandma rings every night to show the cat her dinner."


def main() -> None:
    # The gate requires 1-280 UTF-8 characters, not only whitespace.
    text = SCENE.strip()
    if not (1 <= len(text) <= 280) or not text.strip():
        raise ValueError("entry text fails the 1-280 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
