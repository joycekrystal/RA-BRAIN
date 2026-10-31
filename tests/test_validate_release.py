import importlib.util
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location(
    'release', Path(__file__).resolve().parents[1] / 'scripts/validate_release.py')
release = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(release)


class ReleaseTests(unittest.TestCase):
    old_log = '# Release notes\n\n## 0.2.0 — 2026-10-31\n\n- Existing history.\n'

    def check(self, kind='patch', new='0.2.1', mismatched=False, history=True, dated=True):
        base = {'name': 'business-to-build', 'version': '0.2.0'}
        manifests = [dict(base, version=new) for _ in range(3)]
        if mismatched:
            manifests[1]['version'] = '0.2.0'
        log = (f'# Release notes\n\n## {new} — 2026-10-31\n\n'
               f'Release type: {kind}\nRationale: Test classification.\n\n'
               f'- {"2026-10-31: " if dated else ""}Change.\n')
        log += self.old_log[self.old_log.index('\n## '):] if history else ''
        return release.validate(base, manifests, self.old_log, log, f'Version: {new}')

    def test_each_bump(self):
        for kind, new in [('patch', '0.2.1'), ('minor', '0.3.0'), ('major', '1.0.0')]:
            with self.subTest(kind=kind):
                self.assertIn(new, self.check(kind, new))

    def test_missing_wrong_or_skipped_bump(self):
        for kind, new in [('patch', '0.2.0'), ('minor', '0.2.1'), ('patch', '0.2.2')]:
            with self.subTest(new=new), self.assertRaises(ValueError):
                self.check(kind, new)

    def test_manifest_mismatch(self):
        with self.assertRaises(ValueError):
            self.check(mismatched=True)

    def test_history_and_dates_required(self):
        for options in [{'history': False}, {'dated': False}]:
            with self.subTest(options=options), self.assertRaises(ValueError):
                self.check(**options)

    def test_non_normal_versions_rejected(self):
        for value in ['01.2.3', '1.2', '1.2.3+meta', '1.2.3-rc.1']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                release.version(value)


if __name__ == '__main__':
    unittest.main()
