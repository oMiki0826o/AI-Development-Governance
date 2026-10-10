"""
tests/test_bootstrap.py

Modification():
- 1.2.0: Exercise the real bootstrap output, no-overwrite rules, dry run and safety.
"""

from __future__ import annotations

import hashlib
import importlib.util
import shutil
from unittest import mock
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/bootstrap_project.py'


class BootstrapTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.target = Path(self.tmp.name) / 'project'
        self.target.mkdir()

    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), str(self.target), *args],
                              capture_output=True, text=True, timeout=20)

    def test_all_mode_language_combinations(self):
        for mode in ('minimal', 'standard', 'full'):
            for lang in ('zh-TW', 'en', 'bilingual'):
                with self.subTest(mode=mode, lang=lang):
                    root = self.target / f'{mode}-{lang}'
                    root.mkdir()
                    out = subprocess.run([sys.executable, str(SCRIPT), str(root),
                                          '--mode', mode, '--language', lang],
                                         capture_output=True, text=True, timeout=20)
                    self.assertEqual(out.returncode, 0, out.stderr)
                    languages = ('zh-TW', 'en') if lang == 'bilingual' else (lang,)
                    for language in languages:
                        self.assertTrue((root / '.governance' / language / 'rules/core.md').is_file())
                        self.assertTrue((root / '.governance' / language / 'rules/decision.md').is_file())
                        self.assertTrue((root / '.governance' / language / 'workflows/task-lifecycle.md').is_file())
                        self.assertFalse((root / '.governance' / language / '.governance').exists())
                    self.assertTrue((root / '.governance/manifest.json').is_file())
                    self.assertIn('data/', (root / '.gitignore').read_text())
                    self.assertIn('.governance/', (root / 'AGENTS.md').read_text())
                    self.assertTrue((root / 'data/ai/project-memory.md').exists())
                    if mode == 'minimal':
                        self.assertFalse((root / '.governance' / languages[0] / 'gates').exists())
                    if mode == 'full':
                        self.assertTrue((root / '.governance' / languages[0] / 'docs/architecture.md').exists())

    def test_manifest_hashes_match_written_files(self):
        self.assertEqual(self.run_cli('--mode', 'standard').returncode, 0)
        doc = json.loads((self.target / '.governance/manifest.json').read_text())
        self.assertEqual(doc['governance_version'], '1.2.0')
        self.assertEqual(doc['language'], 'zh-TW')
        self.assertIsInstance(doc['managed_files'], dict)
        for path, expected in doc['managed_files'].items():
            actual = hashlib.sha256((self.target / path).read_bytes()).hexdigest()
            self.assertEqual(actual, expected, path)

    def test_dry_run_no_files_written(self):
        output = self.run_cli('--mode', 'full', '--language', 'bilingual', '--dry-run')
        self.assertEqual(output.returncode, 0, output.stderr)
        self.assertEqual(list(self.target.iterdir()), [])

    def test_existing_agents_never_clobbered_by_default(self):
        (self.target / 'AGENTS.md').write_text('existing\n')
        output = self.run_cli()
        self.assertNotEqual(output.returncode, 0)
        self.assertEqual((self.target / 'AGENTS.md').read_text(), 'existing\n')
        self.assertFalse((self.target / '.governance').exists())

    def test_force_can_replace_agents_but_not_local_notes(self):
        self.assertEqual(self.run_cli().returncode, 0)
        original = self.target / 'data/ai/project-memory.md'
        original.write_text('USER NOTES: KEEP\n')
        result = self.run_cli('--force', '--mode', 'full')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(original.read_text(), 'USER NOTES: KEEP\n')
        self.assertTrue((self.target / '.governance/zh-TW/rules/release.md').exists())

    def test_no_force_avoids_partial_changes(self):
        first = self.run_cli()
        self.assertEqual(first.returncode, 0, first.stderr)
        output = self.run_cli('--mode', 'standard')
        self.assertNotEqual(output.returncode, 0)
        self.assertFalse((self.target / '.governance/zh-TW/gates/pre-edit.md').exists())

    def test_gitignore_is_appended_not_replaced(self):
        p = self.target / '.gitignore'
        p.write_text('node_modules/\n.env\n')
        self.assertEqual(self.run_cli().returncode, 0)
        text = p.read_text()
        self.assertTrue(text.startswith('node_modules/\n.env\n'))
        self.assertEqual(text.count('\ndata/'), 1)

    def test_gitignore_line_endings_preserved(self):
        p = self.target / '.gitignore'
        p.write_bytes(b'node_modules/\r\n.env\r\n')
        self.assertEqual(self.run_cli().returncode, 0)
        self.assertEqual(p.read_bytes().replace(b'\r\n', b'' ).find(b'\n'), -1)
        self.assertIn(b'data/\r\n', p.read_bytes())

    def test_existing_gitignore_policy_does_not_duplicate(self):
        p = self.target / '.gitignore'
        p.write_text('data/\n')
        self.assertEqual(self.run_cli().returncode, 0)
        self.assertEqual(p.read_text(), 'data/\n')

    def test_exception_to_data_ignore_rejected(self):
        p = self.target / '.gitignore'
        p.write_text('data/\n!data/ai/file.md\n')
        result = self.run_cli()
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.target / 'AGENTS.md').exists())

    def test_existing_local_memory_is_preserved(self):
        f = self.target / 'data/ai/project-memory.md'
        f.parent.mkdir(parents=True)
        f.write_text('keep me\n')
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(f.read_text(), 'keep me\n')

    @unittest.skipUnless(hasattr(__import__('os'), 'symlink'), 'symlinks not supported')
    def test_symlink_destination_is_rejected(self):
        elsewhere = Path(self.tmp.name) / 'elsewhere'
        elsewhere.mkdir()
        (self.target / '.governance').symlink_to(elsewhere, target_is_directory=True)
        result = self.run_cli('--mode', 'full')
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(list(elsewhere.iterdir()))

    def test_missing_target_reports_error(self):
        result = subprocess.run([sys.executable, str(SCRIPT), str(self.target / 'not-found')],
                                capture_output=True, text=True, timeout=20)
        self.assertEqual(result.returncode, 2)

    def test_real_git_ignore_policy(self):
        if shutil.which('git') is None:
            self.skipTest('Git is not installed')
        subprocess.run(['git', 'init', '-q', str(self.target)], check=True)
        result = self.run_cli('--mode', 'minimal')
        self.assertEqual(result.returncode, 0, result.stderr)
        check = subprocess.run(['git', '-C', str(self.target), 'check-ignore', '-q', 'data/ai/project-memory.md'])
        self.assertEqual(check.returncode, 0)

    def test_transaction_rolls_back_changed_files(self):
        spec = importlib.util.spec_from_file_location('governance_bootstrap', SCRIPT)
        bootstrap = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(bootstrap)
        a = self.target / '.gitignore'
        b = self.target / 'AGENTS.md'
        a.write_bytes(b'old ignore\n')
        b.write_bytes(b'old agent\n')
        real_replace = bootstrap.os.replace
        n = 0

        def fail_second(source, dest):
            nonlocal n
            n += 1
            if n == 2:
                raise OSError('simulated disk failure')
            return real_replace(source, dest)

        with mock.patch.object(bootstrap.os, 'replace', side_effect=fail_second):
            with self.assertRaises(OSError):
                bootstrap.apply_plan(self.target, {'.gitignore': b'new ignore\n', 'AGENTS.md': b'new agent\n'})
        self.assertEqual(a.read_bytes(), b'old ignore\n')
        self.assertEqual(b.read_bytes(), b'old agent\n')
        self.assertFalse(list(self.target.glob('.governance-*')))

    def test_source_target_rejected(self):
        out = subprocess.run([sys.executable, str(SCRIPT), str(ROOT)], capture_output=True, text=True)
        self.assertEqual(out.returncode, 2)


if __name__ == '__main__':
    unittest.main()
