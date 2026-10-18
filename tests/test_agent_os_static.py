"""Unit tests for offline agent blueprint verifier. No network or external apps."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from verify_agent_os import validate_skill, validate_tree  # noqa: E402


class AgentBlueprintTests(unittest.TestCase):
    def test_real_blueprint_is_structurally_valid(self) -> None:
        self.assertEqual([], validate_tree())

    def test_inert_fake_skill_without_frontmatter_is_rejected(self) -> None:
        self.assertTrue(validate_skill("# skill\nI claim everything passed.", "fake-skill"))

    def test_wrong_skill_name_is_rejected(self) -> None:
        data = "---\nname: other-skill\ndescription: Use for validating a real agent state before any work\n---\n" + (
            "\n## Activation\n## Required preflight\n## Procedure\n## Security\n"
            "## Test-first\n## Evidence\n## Independent assessor\n"
            "## Canonical references\n" + ("example " * 300) +
            "docs/agent-os/07-EVIDENCE.md"
        )
        self.assertIn("fake-skill: frontmatter name mismatch", validate_skill(data, "fake-skill"))


if __name__ == "__main__":
    unittest.main()
