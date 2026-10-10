"""Rebuild the module index in the README from each module's docstring header

Usage: python scripts/regenerate_index.py
"""

from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "math_in_python"
README = ROOT / "README.md"
START, END = "<!-- INDEX:START -->", "<!-- INDEX:END -->"


def header_fields(path: Path) -> dict[str, str]:
    doc = ast.get_docstring(ast.parse(path.read_text())) or ""
    lines = doc.splitlines()
    fields = {"title": lines[0].strip() if lines else path.stem}
    for line in lines[1:]:
        for key in ("Complexity",):
            if line.startswith(f"{key}:"):
                fields[key.lower()] = line.split(":", 1)[1].strip()
    return fields


def build() -> str:
    rows = ["| Topic | Module | Complexity |", "|---|---|---|"]
    for path in sorted(SRC.rglob("*.py")):
        if path.name == "__init__.py":
            continue
        f = header_fields(path)
        rel = path.relative_to(ROOT).as_posix()
        domain = path.parent.name
        rows.append(
            f"| {f['title']} | [`{domain}/{path.stem}`]({rel}) | "
            f"{f.get('complexity', '')} |"
        )
    return "\n".join(rows)


def main() -> None:
    text = README.read_text()
    block = f"{START}\n{build()}\n{END}"
    if START in text and END in text:
        head, rest = text.split(START, 1)
        _, tail = rest.split(END, 1)
        text = head + block + tail
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    README.write_text(text)


if __name__ == "__main__":
    main()
