#!/usr/bin/env python3
"""Offline structural verification for the AGENT BLUEPRINT ONLY.
Not Antigravity installation, security, runtime, browser, or load verification.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_LOCAL_SKILLS = {
    "agent-bootcamp", "source-verification", "spec-kit-orchestration",
    "rootcause-debugging", "test-first-engineering", "independent-review",
    "reproducible-release", "continuous-improvement",
    "medusa-capability-mapping", "medusa-domain-module", "medusa-workflow",
    "next-storefront", "medusa-admin", "postgres-migrations",
    "security-audit", "qa-browser-evidence", "performance-sre",
    "deploy-operations", "ksa-localization", "cms-page-builder",
}
GATE_DOCS = [
    "AGENTS.md", "README.md", "START_AGENT_AR.md",
    ".specify/memory/constitution.md",
    *[f"docs/agent-os/{p}" for p in (
        "README.md", "01-UPSTREAM-AUDIT.md", "02-INSTALL.md",
        "03-CURRICULUM.md", "04-CERTIFICATION-GATES.md",
        "05-ROUTER.md", "06-DEBUGGING.md", "07-EVIDENCE.md",
        "08-LEARNING-LOOP.md", "09-SDD.md", "10-SECURITY-LABS.md",
        "11-ANTIGRAVITY.md", "12-READING-LIST.md", "STATUS.md")],
    "specs/000-agent-readiness/spec.md",
    "specs/000-agent-readiness/plan.md",
    "specs/000-agent-readiness/tasks.md",
    "tasks/F00-BASELINE.md",
]
REQUIRED_SECTIONS = [
    "## Activation", "## Required preflight", "## Procedure",
    "## Security", "## Test-first", "## Evidence", "## Independent assessor",
    "## Canonical references",
]


def validate_skill(body: str, dirname: str) -> list[str]:
    errors: list[str] = []
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", body, re.S)
    if not match:
        return [f"{dirname}: missing SKILL.md YAML frontmatter"]
    header = match.group(1)
    if f"name: {dirname}" not in header:
        errors.append(f"{dirname}: frontmatter name mismatch")
    desc = re.search(r"^description:\s*(.+)$", header, flags=re.M)
    if not desc or len(desc.group(1).strip()) < 35:
        errors.append(f"{dirname}: missing informative activation description")
    for section in REQUIRED_SECTIONS:
        if section not in body:
            errors.append(f"{dirname}: missing section {section}")
    if len(body) < 1250:
        errors.append(f"{dirname}: superficial skill body (<1250 chars)")
    if "docs/agent-os/07-EVIDENCE.md" not in body:
        errors.append(f"{dirname}: missing evidence framework")
    return errors


def validate_tree(root: Path = ROOT) -> list[str]:
    errors = []
    for rel in GATE_DOCS:
        p = root / rel
        if not p.is_file() or not p.read_text(encoding="utf-8").strip():
            errors.append(f"missing/empty required file: {rel}")
    skills_dir = root / ".agents" / "skills"
    for dirname in REQUIRED_LOCAL_SKILLS:
        path = skills_dir / dirname / "SKILL.md"
        if not path.exists():
            errors.append(f"missing local skill: {path.relative_to(root)}")
        else:
            errors.extend(validate_skill(path.read_text(encoding="utf-8"), dirname))
    if not errors:
        spec = (root / "specs/000-agent-readiness/spec.md").read_text()
        tasks = (root / "specs/000-agent-readiness/tasks.md").read_text()
        status = (root / "docs/agent-os/STATUS.md").read_text()
        constitution = (root / ".specify/memory/constitution.md").read_text()
        for i in range(1, 11):
            if f"AR-{i:03d}" not in spec:
                errors.append(f"missing requirement AR-{i:03d}")
        for i in range(8):
            if f"AG{i:02d}" not in tasks or f"AG{i:02d}" not in status:
                errors.append(f"missing training stage AG{i:02d}")
        if not re.search(r"\|\s*AG07\s*\|[^|]*\|\s*NOT_STARTED\s*\|", status):
            errors.append("AG07 must be explicitly NOT_STARTED until verified externally")
        if not re.search(r"\|\s*F00\s*\|[^|]*\|\s*LOCKED\s*\|", status):
            errors.append("F00 must be LOCKED until AG07 passes")
        if "Medusa" not in constitution or "Spec" not in constitution:
            errors.append("constitution missing Medusa/Spec constraints")
        if "AG00" not in (root / "START_AGENT_AR.md").read_text():
            errors.append("entry prompt must authorize AG00, not F00")
    return errors


def main() -> int:
    errors = validate_tree()
    if errors:
        for item in errors:
            print(f"FAIL: {item}", file=sys.stderr)
        return 1
    print(f"PASS: Offline agent blueprint integrity ({len(REQUIRED_LOCAL_SKILLS)} curated local skills).")
    print("NOT RUN: Antigravity tools, external plugin installation, Medusa app, browser, security, load.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
