#!/usr/bin/env python3
"""Safely copy selected Studios.Bit skills into another Codex project.

No network calls, no target file overwrites, and no app deployment.
"""

from __future__ import annotations

import argparse
import pathlib
import shutil
import sys

SOURCE = pathlib.Path(__file__).resolve().parent.parent
WEB_DEFAULTS = (
    "director-proyecto",
    "arquitectura-web",
    "diseno-sitios-web",
    "frontend-ingenieria",
    "ciberseguridad-web",
    "bitproof-qa",
)


def plan(target: pathlib.Path, names: list[str], source: pathlib.Path = SOURCE) -> list[tuple[pathlib.Path, pathlib.Path]]:
    available = {p.name for p in (source / "skills").iterdir() if (p / "SKILL.md").is_file()}
    invalid = set(names) - available
    if invalid:
        raise ValueError(f"Unknown skill(s): {', '.join(sorted(invalid))}. Available: {', '.join(sorted(available))}")
    root = target / ".agents"
    copies = [(source / "skills" / name, root / "skills" / name) for name in names]
    copies.extend([(source / "references", root / "references"),
                   (source / "templates", root / "templates")])
    for src, _ in copies:
        if not src.is_dir():
            raise ValueError(f"Missing source folder: {src}")
    for _, dst in copies:
        if dst.exists():
            raise ValueError(f"Destination exists, refusing overwrite: {dst}")
    return copies


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=pathlib.Path, help="Existing local project directory")
    parser.add_argument("--skills", nargs="+", help="Skill folder names. Defaults to web starter set")
    parser.add_argument("--list", action="store_true", help="List available names and exit")
    parser.add_argument("--dry-run", action="store_true", help="Preview copies without changes")
    args = parser.parse_args()
    if args.list:
        print("\n".join(sorted(p.name for p in (SOURCE / "skills").iterdir() if (p / "SKILL.md").is_file())))
        return 0
    if args.target is None:
        parser.error("--target is required unless --list is used")
    target = args.target.resolve()
    if not target.is_dir():
        parser.error(f"Target is not an existing directory: {target}")
    names = list(dict.fromkeys(args.skills or WEB_DEFAULTS))
    try:
        copies = plan(target, names)
    except ValueError as exc:
        print(f"ABORT: {exc}", file=sys.stderr)
        return 2
    for src, dst in copies:
        print(f"{'PLAN' if args.dry_run else 'COPY'}: {src.relative_to(SOURCE)} → {dst}")
        if not args.dry_run:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(src, dst)
    print("Done. Add project-specific routing to the target AGENTS.md manually.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
