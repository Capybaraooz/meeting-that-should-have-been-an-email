"""The Meeting That Should Have Been an Email — make.fun entry.

Writes one line (<=200 chars) to /output/entry.txt.
"""
import os

LINE = "This meeting has 14 people, 3 agendas, and one sentence that could have been an email: 'Let's meet again Thursday.'".strip()
assert "\n" not in LINE, "entry line must be a single line"

def main():
    assert len(LINE) <= 200, "entry line must be at most 200 chars"
    out = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)
    print(LINE)

if __name__ == "__main__":
    main()
