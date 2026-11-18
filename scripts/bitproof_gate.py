#!/usr/bin/env python3
"""Validate BitProof evidence records and report release blockers.

This is a DOCUMENTATION gate, not a security/accessibility test runner.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import sys

BASE = {"UX-01", "UI-01", "A11Y-01", "PERF-01", "SEC-01", "OPS-01"}
REQUIRED = {"S": BASE, "M": BASE | {"API-01", "PRIV-01"},
            "A": BASE | {"API-01", "PRIV-01", "SEC-02", "DB-01"}}
STATUSES = {"pass", "fail", "pending", "na"}
METHODS = {"auto", "manual", "usuario", "tercero"}


def check_evidence(data: object) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    blockers: list[str] = []
    if not isinstance(data, dict):
        return ["root must be a JSON object"], []
    risk = data.get("risk")
    if risk not in REQUIRED:
        return ["risk must be S, M or A"], []
    if not isinstance(data.get("project"), str) or not data["project"].strip():
        errors.append("project must be non-empty")
    if not isinstance(data.get("environment"), str) or not data["environment"].strip():
        errors.append("environment must be non-empty")
    checks = data.get("checks")
    if not isinstance(checks, list):
        return errors + ["checks must be an array"], []
    seen: set[str] = set()
    for idx, check in enumerate(checks):
        if not isinstance(check, dict):
            errors.append(f"checks[{idx}] must be an object")
            continue
        cid = check.get("id")
        if not isinstance(cid, str) or not cid.strip():
            errors.append(f"checks[{idx}].id required")
            continue
        if cid in seen:
            errors.append(f"duplicate id {cid}")
        seen.add(cid)
        status = check.get("status")
        if status not in STATUSES:
            errors.append(f"{cid}: invalid status '{status}'")
            continue
        if not isinstance(check.get("blocker"), bool):
            errors.append(f"{cid}: blocker must be boolean")
            continue
        if status in ("pass", "fail"):
            if check.get("method") not in METHODS:
                errors.append(f"{cid}: executed check needs method")
            if not isinstance(check.get("owner"), str) or not check["owner"].strip():
                errors.append(f"{cid}: executed check needs owner")
            ts = check.get("executed_at")
            try:
                if not isinstance(ts, str):
                    raise ValueError("missing timestamp")
                value = dt.datetime.fromisoformat(ts.replace("Z", "+00:00"))
                if value.tzinfo is None:
                    raise ValueError("timestamp requires timezone")
            except ValueError:
                errors.append(f"{cid}: executed check needs ISO 8601 timezone timestamp")
            evidence = check.get("evidence")
            if not isinstance(evidence, list) or not evidence or not all(isinstance(item, str) and item.strip() for item in evidence):
                errors.append(f"{cid}: executed check needs evidence path(s) or URL(s)")
            if status == "fail" and not str(check.get("note", "")).strip():
                errors.append(f"{cid}: failing check needs issue note")
        elif status == "na":
            if not str(check.get("note", "")).strip():
                errors.append(f"{cid}: not-applicable requires reason")
            if cid in REQUIRED[risk] and not str(check.get("reviewer", "")).strip():
                errors.append(f"{cid}: required gate N/A needs named reviewer")
        if check["blocker"] and status in ("fail", "pending"):
            blockers.append(f"{cid} ({status})")

    for cid in sorted(REQUIRED[risk] - seen):
        errors.append(f"required gate absent for risk {risk}: {cid}")
    # A missing or optional check must not trick consumers into a green result.
    for cid in sorted(REQUIRED[risk] & seen):
        check = next((c for c in checks if isinstance(c, dict) and c.get("id") == cid), {})
        if check.get("blocker") is False and check.get("status") != "na":
            errors.append(f"{cid}: required gate cannot be marked non-blocking")
        if check.get("status") == "na" and not str(check.get("note", "")).strip():
            errors.append(f"{cid}: required na needs reason")
    return errors, blockers


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--file", type=pathlib.Path, required=True, help="JSON BitProof evidence document")
    args = ap.parse_args()
    try:
        data = json.loads(args.file.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"NO-GO: cannot read evidence: {exc}", file=sys.stderr)
        return 2
    errors, blockers = check_evidence(data)
    for issue in errors:
        print(f"INVALID: {issue}")
    for issue in blockers:
        print(f"BLOCKER: {issue}")
    if errors or blockers:
        print("NO-GO (metadata/evidence declaration only)")
        return 1
    print("GO técnico documental — no equivale a tests ejecutados por este script ni autoriza deployment")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
