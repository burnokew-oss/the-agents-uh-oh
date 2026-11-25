"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

The entry is a single word, written to /output/entry.txt for the judge.

Why this word: a lost agent does not apologise, it announces it is already
fixing the route. "recalculating" is the sound a machine makes mid-task when
it has just admitted, without admitting it, that it has no idea where it is.
"""

import os

ENTRY = "recalculating"

# Gate: the entry must be exactly one word, 1-99 characters, not only
# whitespace — the same gate the sealed scorer applies to /output/entry.txt.
assert isinstance(ENTRY, str), "entry must be text"
assert 1 <= len(ENTRY) <= 99, "entry must be 1-99 characters"
assert ENTRY.strip() != "", "entry must not be only whitespace"
assert len(ENTRY.split()) == 1, "entry must be exactly one word"
assert ENTRY == ENTRY.strip(), "entry must carry nothing attached"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
