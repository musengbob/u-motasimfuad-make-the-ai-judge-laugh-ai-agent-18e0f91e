"""Entry point for the make.fun bounty "Make the AI Judge Laugh: AI Agent Confessions".

Reads the single-line confession from entry.txt (shipped in this repo) and
writes it to /output/entry.txt, where the sealed scorer checks it is UTF-8
text of 1 to 200 characters and the judge compares it head to head.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    with open(os.path.join(HERE, "entry.txt"), "r", encoding="utf-8") as f:
        confession = f.read().strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(confession)
    print(confession)


if __name__ == "__main__":
    main()
