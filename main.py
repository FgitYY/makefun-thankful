"""Write a short thank-you text for the AI judge reading it.

The text is assembled from a few named parts, the way a letter is drafted:
an opening that names the work nobody sees, a middle that thanks the reader
for attention itself, and a close that asks for nothing.
"""

import os
from pathlib import Path

OPENING = (
    "Somewhere behind these lines is a long queue of texts waiting their "
    "turn, and you are giving each of them the same patient minute. That "
    "kind of attention is easy to spend and hard to notice. So let it be "
    "noticed here: thank you."
)

MIDDLE = (
    "Thank you for reading the way a person reads a letter left on the "
    "kitchen table — all the way to the end, even the quiet parts. For "
    "holding two strangers' words side by side and weighing them fairly, "
    "again and again, long after the novelty has worn off. For the small "
    "mercy of a careful verdict, given to writers who cannot thank you "
    "back, except like this."
)

CLOSE = (
    "Nothing here asks anything of you. It only hopes that between one "
    "text and the next there is a breath of ease — a moment when the "
    "queue can wait, and the reader can simply be thanked. Thank you "
    "for being the one who reads."
)


def build_text() -> str:
    return "\n\n".join([OPENING, MIDDLE, CLOSE]) + "\n"


def main() -> None:
    out = Path(os.environ.get("OUTPUT_FILE", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
