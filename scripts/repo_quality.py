#!/usr/bin/env python3
"""Validate the Studios.Bit knowledge repository without network/dependencies.

This validates skill metadata, required links, and library structure. It does
not assess real-world UX, security, accessibility, or client site quality.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
from urllib.parse import unquote


MD_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_TOP = ("README.md", "AGENTS.md", "docs/INSTALACION_CODEX.md")


def check_repository(root: pathlib.Path) -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED_TOP:
        if not (root / rel).is_file():
            errors.append(f"Missing top-level file: {rel}")

    skills = sorted((root / "skills").glob("*/SKILL.md"))
    if not skills:
        errors.append("No skills/*/SKILL.md files")

    names: set[str] = set()
    for path in skills:
        rel = path.relative_to(root).as_posix()
        body = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", body, re.DOTALL)
        if not match:
            errors.append(f"{rel}: missing frontmatter")
            continue
        fields: dict[str, str] = {}
        for line in match.group(1).splitlines():
            if not line.strip():
                continue
            if ":" not in line:
                errors.append(f"{rel}: malformed frontmatter line: {line}")
                continue
            key, val = line.split(":", 1)
            fields[key.strip()] = val.strip().strip('"').strip("'")
        if set(fields) != {"name", "description"}:
            errors.append(f"{rel}: frontmatter must have name and description only")
        name = fields.get("name", "")
        if not SKILL_NAME.fullmatch(name):
            errors.append(f"{rel}: invalid skill name '{name}'")
        if name in names:
            errors.append(f"{rel}: duplicate skill name '{name}'")
        names.add(name)
        if len(fields.get("description", "")) < 35:
            errors.append(f"{rel}: description too short to trigger reliably")
        if len(body.splitlines()) > 500:
            errors.append(f"{rel}: skill exceeds progressive-disclosure target of 500 lines")

    markdowns = sorted(root.rglob("*.md"))
    for path in markdowns:
        # Avoid build/cache output from an unrelated local checkout.
        if any(part.startswith(".") and part not in (".github", ".agents") for part in path.relative_to(root).parts):
            continue
        rel = path.relative_to(root).as_posix()
        content = path.read_text(encoding="utf-8")
        for raw_target in MD_LINK.findall(content):
            target = raw_target.strip().split(" ", 1)[0].split("#", 1)[0]
            if not target or target.startswith(("https://", "http://", "mailto:", "tel:", "data:")):
                continue
            if target.startswith(("/", "../..//")):
                errors.append(f"{rel}: absolute/unexpected local link '{raw_target}'")
                continue
            resolved = (path.parent / unquote(target)).resolve()
            if not resolved.is_relative_to(root.resolve()):
                errors.append(f"{rel}: link escapes repository '{raw_target}'")
            elif not resolved.exists():
                errors.append(f"{rel}: broken link '{raw_target}'")

    readme = (root / "README.md")
    if readme.is_file():
        content = readme.read_text(encoding="utf-8")
        for skill in skills:
            rel = skill.relative_to(root).as_posix()
            if rel not in content:
                errors.append(f"README.md does not index {rel}")

    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parent.parent)
    args = ap.parse_args()
    root = args.root.resolve()
    errors = check_repository(root)
    if errors:
        for error in errors:
            print(f"ERROR {error}", file=sys.stderr)
        print(f"Library validation: FAIL ({len(errors)} issues)", file=sys.stderr)
        return 1
    skills = len(list((root / "skills").glob("*/SKILL.md")))
    markdowns = len(list(root.rglob("*.md")))
    print(f"Library validation: PASS ({skills} skills, {markdowns} Markdown files)")
    print("Scope: metadata, relative links and structure only; not customer-site QA.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
