#!/usr/bin/env python3
"""Fail if active text files contain CJK ideographs.

The repository permits immutable hashes that identify non-English external
artifacts, but active proof and research text must remain in English.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

HAN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
TEXT_SUFFIXES = {
    ".md",
    ".py",
    ".toml",
    ".yml",
    ".yaml",
    ".json",
    ".csv",
    ".txt",
}
EXCLUDED_DIRS = {".git", ".venv"}


def find_violations(root: Path) -> list[str]:
    violations: list[str] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or EXCLUDED_DIRS.intersection(path.parts):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {
            ".gitignore",
            "NO_LICENSE",
        }:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            if HAN.search(line):
                violations.append(f"{path.relative_to(root)}:{line_number}")
    return violations


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    violations = find_violations(args.root.resolve())
    if violations:
        print("ENGLISH_ONLY_TEXT_SCAN_FAIL")
        for item in violations:
            print(item)
        return 1

    print("ENGLISH_ONLY_TEXT_SCAN_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
