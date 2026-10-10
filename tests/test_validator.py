"""
tests/test_validator.py

Modification():
- 1.2.0: Positive and negative tests for repository invariants and validation errors.
"""

from __future__ import annotations

import importlib.util
import contextlib
import io
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('governance_validator', ROOT / 'scripts/validate.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / 'repository'
        shutil.copytree(ROOT, self.path, ignore=shutil.ignore_patterns('__pycache__', '.git', '.venv', '.pytest_cache'))

    def verify(self):
        tool = module.Validator(self.path)
        with contextlib.redirect_stdout(io.StringIO()):
            result = tool.run()
        return result, tool.errors

    def test_repository_validates(self):
        code, errors = self.verify()
        self.assertEqual(code, 0, errors)

    def test_missing_version_does_not_raise(self):
        (self.path / 'VERSION').unlink()
        code, errors = self.verify()
        self.assertNotEqual(code, 0)
        self.assertTrue(any('VERSION' in x for x in errors))

    def test_missing_readme_does_not_raise(self):
        (self.path / 'README.md').unlink()
        code, errors = self.verify()
        self.assertNotEqual(code, 0)
        self.assertTrue(any('README.md' in x for x in errors))

    def test_invalid_utf8_reports_file(self):
        (self.path / 'en/rules/core.md').write_bytes(b'\xff\xfe\x00')
        code, errors = self.verify()
        self.assertNotEqual(code, 0)
        self.assertTrue(any('invalid UTF-8' in x for x in errors))

    def test_unexpected_bom(self):
        p = self.path / 'VERSION'
        p.write_bytes(b'\xef\xbb\xbf1.2.0\n')
        code, errors = self.verify()
        self.assertNotEqual(code, 0)
        self.assertTrue(any('BOM' in x for x in errors))

    def test_image_link_is_checked(self):
        p = self.path / 'README.md'
        p.write_text(p.read_text() + '\n![Missing](images/missing.png)\n')
        code, errors = self.verify()
        self.assertNotEqual(code, 0)
        self.assertTrue(any('broken link' in x for x in errors))

    def test_inline_code_block_with_missing_link_is_skipped(self):
        p = self.path / 'README.md'
        p.write_text(p.read_text() + '\n```markdown\n[Example](missing.md)\n```\n')
        code, errors = self.verify()
        self.assertEqual(code, 0, errors)

    def test_valid_reference_link(self):
        p = self.path / 'README.md'
        p.write_text(p.read_text() + '\n[Guide][intro]\n\n[intro]: QUICKSTART.md\n')
        code, errors = self.verify()
        self.assertEqual(code, 0, errors)

    def test_bad_line_endings(self):
        file = self.path / 'VERSION'
        file.write_bytes(b'1.2.0\r\n')
        code, errors = self.verify()
        self.assertNotEqual(code, 0)
        self.assertTrue(any('CR/CRLF' in x for x in errors))

    def test_missing_final_newline(self):
        (self.path / 'VERSION').write_bytes(b'1.2.0')
        code, errors = self.verify()
        self.assertNotEqual(code, 0)
        self.assertTrue(any('trailing LF' in x for x in errors))

    def test_invalid_semver(self):
        (self.path / 'VERSION').write_text('01.2.0\n')
        code, errors = self.verify()
        self.assertNotEqual(code, 0)
        self.assertTrue(any('SemVer' in x for x in errors))

    def test_valid_semver_variants(self):
        for v in ('1.2.3', '0.0.0', '1.2.3-rc.1+build.7'):
            self.assertTrue(module.SEMVER.fullmatch(v), v)
        for v in ('01.2.3', '1.02.3', '1.2.03', '1.2.3-01', '1.2.3+', '1.2'):
            self.assertFalse(module.SEMVER.fullmatch(v), v)

    def test_nonexistent_rule_reference(self):
        p = self.path / 'zh-TW/workflows/bugfix.md'
        p.write_text(p.read_text() + '\nFollow `CORE-999`.\n')
        code, errors = self.verify()
        self.assertNotEqual(code, 0)
        self.assertTrue(any('unknown Rule ID: CORE-999' in x for x in errors))

    def test_duplicate_rule_id(self):
        p = self.path / 'zh-TW/rules/convergence.md'
        p.write_text(p.read_text() + '\n### CORE-001 — Duplicate\n\nDuplicate.\n')
        code, errors = self.verify()
        self.assertNotEqual(code, 0)
        self.assertTrue(any('duplicate zh-TW rule ID CORE-001' in x for x in errors))

    def test_gate_missing_value(self):
        p = self.path / 'en/gates/pre-edit.md'
        p.write_text(p.read_text().replace('**Actor**: Developer or agent performing this phase', '**Actor**:'))
        code, errors = self.verify()
        self.assertNotEqual(code, 0)
        self.assertTrue(any('Gate metadata: Actor' in x for x in errors))

    def test_gate_malformed_id(self):
        p = self.path / 'en/gates/pre-edit.md'
        p.write_text(p.read_text().replace('GATE-PRE-EDIT', 'gate wrong'))
        code, errors = self.verify()
        self.assertNotEqual(code, 0)
        self.assertTrue(any('malformed Gate ID' in x for x in errors))

    def test_invalid_link(self):
        p = self.path / 'README.md'
        p.write_text(p.read_text() + '\n[Missing](missing-guide.md)\n')
        code, errors = self.verify()
        self.assertNotEqual(code, 0)
        self.assertTrue(any('broken link' in x for x in errors))

    def test_invalid_anchor(self):
        p = self.path / 'README.md'
        p.write_text(p.read_text() + '\n[Missing anchor](#not-a-real-heading)\n')
        code, errors = self.verify()
        self.assertNotEqual(code, 0)
        self.assertTrue(any('broken anchor' in x for x in errors))

    def test_valid_markdown_nested_parentheses(self):
        p = self.path / 'README.md'
        (self.path / 'file(name).md').write_text('# Heading\n')
        p.write_text(p.read_text() + '\n[Working](file(name).md)\n')
        code, errors = self.verify()
        self.assertEqual(code, 0, errors)

    def test_bad_reference_definition(self):
        p = self.path / 'README.md'
        p.write_text(p.read_text() + '\n[Missing][unknown-doc]\n')
        code, errors = self.verify()
        self.assertNotEqual(code, 0)
        self.assertTrue(any('missing Markdown reference' in x for x in errors))

    def test_local_data_is_skipped(self):
        folder = self.path / 'data/ai'
        folder.mkdir(parents=True, exist_ok=True)
        (folder / 'broken.md').write_bytes(b'\xff\x00')
        code, errors = self.verify()
        self.assertEqual(code, 0, errors)

    def test_language_file_mismatch(self):
        (self.path / 'en/docs/architecture.md').unlink()
        code, errors = self.verify()
        self.assertNotEqual(code, 0)
        self.assertTrue(any('language file mismatch' in x for x in errors))

    def test_bad_ignore_policy(self):
        p = self.path / '.gitignore'
        p.write_text(p.read_text() + '\n!data/ai/private.md\n')
        code, errors = self.verify()
        self.assertNotEqual(code, 0)
        self.assertTrue(any('unignore local data' in x for x in errors))


if __name__ == '__main__':
    unittest.main()
