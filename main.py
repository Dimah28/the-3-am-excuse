"""The 3 AM Excuse -- make.fun bounty u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.

Writes a single excuse (183 characters, inside the 200-character gate)
to /output/entry.txt.

The line: a hardware wallet refuses to sign at 3 AM -- not because of
a battery, a firmware update or cold storage, but because it has seen
exactly how the transaction was born eleven minutes ago, in a group
chat called '100X OR BROKE'. The wallet speaks in its own voice, with
its own grudge: it holds the life savings, it sleeps on it, and it
tells the human to come back at noon. The joke only works at 3 AM --
at 3 PM there is no 3 AM impulse buy to refuse.
"""

import os

LINE = (
    "It's 3 AM. You want me to sign for a coin you found eleven minutes "
    "ago in a group chat called '100X OR BROKE.' I hold your life "
    "savings. Unlike you, I sleep on it \u2014 come back at noon."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, gate is 1-200"
    assert text.strip(), "line must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
