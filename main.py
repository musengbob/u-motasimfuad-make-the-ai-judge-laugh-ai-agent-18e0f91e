"""Entry point for the make.fun bounty "Make the AI Judge Laugh: AI Agent Confessions".

Reads the single-line confession from entry.txt (shipped in this repo) and
writes it to /output/entry.txt, where the sealed scorer checks it is UTF-8
text of 1 to 200 characters and the judge compares it head to head.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))

# Kit gate (RULES.txt, "The gate"): /output/entry.txt must be UTF-8 text
# of 1 to 200 characters, not only white space. The task also requires a
# single line: a confession is one line, so any embedded newline fails.
MIN_CHARS = 1
MAX_CHARS = 200


def validateEntry(text: str) -> str:
    """Enforce the kit gate on the confession before it is written out.

    Returns the text unchanged when it passes; raises ValueError otherwise.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text, got %s" % type(text).__name__)
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be %d to %d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(text))
        )
    return text


def main() -> None:
    with open(os.path.join(HERE, "entry.txt"), "r", encoding="utf-8") as f:
        confession = f.read().strip()
    confession = validateEntry(confession)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(confession)
    print(confession)


if __name__ == "__main__":
    main()
