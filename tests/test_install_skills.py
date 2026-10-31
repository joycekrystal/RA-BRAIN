import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location(
    "installer", Path(__file__).resolve().parents[1] / "scripts/install_skills.py")
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.target = Path(self.temp.name)

    def install(self, dry_run=False):
        with contextlib.redirect_stdout(io.StringIO()):
            installer.install(self.target, list(installer.LOCATIONS), dry_run)

    def test_copy_all_hosts_references_and_repeat(self):
        self.install()
        for location in set(installer.LOCATIONS.values()):
            root = self.target / location
            self.assertEqual(len(list(root.glob('*/SKILL.md'))), 6)
            for source in installer.SOURCE.rglob('*'):
                if source.is_file():
                    self.assertEqual((root / source.relative_to(installer.SOURCE)).read_bytes(),
                                     source.read_bytes())
            self.assertTrue((root / 'design-review/../delivery-standards/references/shared-rules.md').is_file())
        self.install()

    def test_dry_run_does_not_write(self):
        self.install(dry_run=True)
        self.assertEqual(list(self.target.iterdir()), [])

    def test_conflict_preflight_preserves_existing_and_other_destinations(self):
        conflict = self.target / '.claude/skills/design-review/SKILL.md'
        conflict.parent.mkdir(parents=True)
        conflict.write_text('local edits')
        with self.assertRaisesRegex(ValueError, 'Existing content differs'):
            self.install()
        self.assertEqual(conflict.read_text(), 'local edits')
        self.assertFalse((self.target / '.agents').exists())

    def test_symlink_destination_refused(self):
        external = self.target / 'elsewhere'
        external.mkdir()
        (self.target / '.agents').symlink_to(external, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'symlink'):
            self.install()
        self.assertEqual(list(external.iterdir()), [])


if __name__ == '__main__':
    unittest.main()
