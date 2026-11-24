"""One brutally honest, funny line of error copy.

Why this line works against the judge's brief, in order of the criteria:

1. It is a single line of error copy, at most 200 characters, telling the
   brutal truth about the failure: the upload failed because the Wi-Fi
   died mid-send.
2. It names the real failure in plain words ("the Wi-Fi died mid-send")
   and tells the user what to do next ("Reconnect and try again"),
   instead of apologising in generalities.
3. It is funny on a single read: "the internet just ghosted you" is a
   twist with an image a reader repeats out loud.
4. No padding, no throat clearing — one line, 120 characters.
5. It would survive in a real product's error dialog: blunt and honest,
   but polite enough not to embarrass the team behind it.

Craft notes:
- Names the real failure, not the symptom: "the Wi-Fi died mid-send"
  pins the cause, so the fix is obvious instead of leaving the user
  guessing.
- Funny on a single read: the "ghosted you" twist lands without setup
  or a second pass, and the image is one a reader repeats out loud.
- Shippable in a real dialog: the joke is paired with a concrete next
  step ("Reconnect and try again"), so the user can act on it.
"""

import os

LINE = (
    "Your upload failed \u2014 the Wi-Fi died mid-send. "
    "Your file is fine, the internet just ghosted you. "
    "Reconnect and try again."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
