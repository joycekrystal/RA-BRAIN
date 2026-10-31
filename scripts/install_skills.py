#!/usr/bin/env python3
"""Copy canonical skills into a workspace without replacing existing content."""

import argparse
from pathlib import Path
import sys


SOURCE = Path(__file__).resolve().parents[1] / "skills"
LOCATIONS = {"codex": ".agents/skills", "antigravity": ".agents/skills",
             "claude": ".claude/skills"}


def install(target, assistants, dry_run=False):
    target = Path(target).expanduser().resolve()
    if not target.is_dir():
        raise ValueError(f"Workspace must be an existing directory: {target}")
    sources = sorted(SOURCE.glob("*/SKILL.md"))
    if not sources:
        raise ValueError(f"No skills found in {SOURCE}")
    files = []
    for skill in sources:
        files.extend(p for p in sorted(skill.parent.rglob("*")) if p.is_file())
    plan = []
    # Preflight every destination before writing anything. Refuse symlink paths
    # so installation cannot unexpectedly modify a different directory.
    for location in sorted({LOCATIONS[a] for a in assistants}):
        for source in files:
            destination = target / location / source.relative_to(SOURCE)
            for part in (destination, *destination.parents):
                if part == target:
                    break
                if part.is_symlink():
                    raise ValueError(f"Refusing symlink destination: {part}")
                if part != destination and part.exists() and not part.is_dir():
                    raise ValueError(f"Parent is not a directory: {part}")
            if destination.exists():
                if not destination.is_file() or destination.read_bytes() != source.read_bytes():
                    raise ValueError(f"Existing content differs; reconcile manually: {destination}")
            else:
                plan.append((source, destination))
    for source, destination in plan:
        print(f"{'Would copy' if dry_run else 'Copy'} {destination}")
        if not dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            with destination.open("xb") as output:
                output.write(source.read_bytes())
    print(f"{len(sources)} skills; {len(plan)} files {'planned' if dry_run else 'copied'}.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, type=Path, help="Existing application workspace")
    parser.add_argument("--assistants", nargs="+", choices=sorted(LOCATIONS),
                        default=list(LOCATIONS), help="Default: all three assistants")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        install(args.target, args.assistants, args.dry_run)
    except (ValueError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
