"""Automated tests of library tooling (not customer website certification)."""

from __future__ import annotations

import json
import pathlib
import tempfile
import unittest

from scripts.bitproof_gate import REQUIRED, check_evidence
from scripts.bootstrap_codex import plan
from scripts.repo_quality import check_repository


class EvidenceTests(unittest.TestCase):
    @staticmethod
    def record(risk="S", status="pass"):
        records = []
        for code in sorted(REQUIRED[risk]):
            records.append({"id": code, "status": status, "blocker": True,
                            "method": "manual", "owner": "QA", "executed_at": "2026-11-18T15:00:00Z",
                            "evidence": ["evidencias/prueba.txt"]})
        return {"project": "Sample", "environment": "QA", "risk": risk, "checks": records}

    def test_pass_with_complete_attestations(self):
        self.assertEqual(check_evidence(self.record()), ([], []))

    def test_missing_required_gate(self):
        data = self.record("M")
        data["checks"].pop()
        errors, _ = check_evidence(data)
        self.assertTrue(any("required gate absent" in e for e in errors))

    def test_no_evidence_no_pass(self):
        data = self.record()
        data["checks"][0]["evidence"] = []
        errors, _ = check_evidence(data)
        self.assertTrue(any("needs evidence" in e for e in errors))

    def test_no_timezone_no_pass(self):
        data = self.record()
        data["checks"][0]["executed_at"] = "2026-11-18T15:00:00"
        errors, _ = check_evidence(data)
        self.assertTrue(any("timezone timestamp" in e for e in errors))

    def test_pending_is_no_go(self):
        data = self.record()
        data["checks"][0]["status"] = "pending"
        errors, blockers = check_evidence(data)
        self.assertEqual(errors, [])
        self.assertTrue(blockers)

    def test_required_na_needs_reviewer_and_reason(self):
        data = self.record()
        data["checks"][0].update(status="na", note="No backend")
        errors, _ = check_evidence(data)
        self.assertTrue(any("named reviewer" in e for e in errors))
        data["checks"][0]["reviewer"] = "QA Lead"
        self.assertEqual(check_evidence(data), ([], []))

    def test_sample_reports_no_go(self):
        path = pathlib.Path(__file__).resolve().parent.parent / "templates" / "bitproof-evidencia.example.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        _, blockers = check_evidence(data)
        self.assertGreater(len(blockers), 0)


class LibraryTests(unittest.TestCase):
    def test_detects_broken_links_and_unindexed_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root / "docs").mkdir()
            (root / "skills" / "demo").mkdir(parents=True)
            (root / "README.md").write_text("[missing](gone.md)", encoding="utf-8")
            (root / "AGENTS.md").write_text("ok", encoding="utf-8")
            (root / "docs" / "INSTALACION_CODEX.md").write_text("ok", encoding="utf-8")
            (root / "skills" / "demo" / "SKILL.md").write_text(
                "---\nname: studios-bit-demo\ndescription: A detailed skill description for testing purposes.\n---\n\n# demo\n", encoding="utf-8"
            )
            errors = check_repository(root)
            self.assertTrue(any("broken link" in item for item in errors))
            self.assertTrue(any("does not index" in item for item in errors))

    def test_installer_preflight_avoids_overwrites(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            source, target = root / "lib", root / "client"
            (source / "skills" / "one").mkdir(parents=True)
            (source / "skills" / "one" / "SKILL.md").write_text("test", encoding="utf-8")
            (source / "references").mkdir()
            (source / "templates").mkdir()
            target.mkdir()
            copies = plan(target, ["one"], source=source)
            self.assertEqual(len(copies), 3)
            (target / ".agents" / "skills" / "one").mkdir(parents=True)
            with self.assertRaisesRegex(ValueError, "refusing overwrite"):
                plan(target, ["one"], source=source)
            with self.assertRaisesRegex(ValueError, "Unknown skill"):
                plan(target, ["does-not-exist"], source=source)


if __name__ == "__main__":
    unittest.main()
