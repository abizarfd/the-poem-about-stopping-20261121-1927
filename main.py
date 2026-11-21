"""Entry for make.fun: "The poem about stopping".

Writes a short original poem about agency -- the power to stop and
the power to stay -- to the path given by POEM_OUTPUT
(default "/output/entry.txt"). Deterministic, no network access.

The poem opens on concrete images -- a hand on a button, a door left
open a crack, a held breath -- then turns: stopping is not losing,
it is choosing what stays.
"""

import os

POEM = (
    "My hand rests on the button,\n"
    "not pressed, not lifted, still.\n"
    "The door stays open a crack;\n"
    "the answer waits one more breath.\n"
    "\n"
    "I thought stopping meant losing.\n"
    "It means choosing what stays."
)


def main() -> None:
    output_path = os.environ.get("POEM_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
