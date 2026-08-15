#!/usr/bin/env python3
"""Deterministically inventory Agent Skill packages."""

import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Deterministic Agent Skill package inventory")
parser.add_argument("root", nargs="?", default=".")
args = parser.parse_args()

skills_root = Path(args.root) / ".agents" / "skills"
for skill_dir in sorted(path for path in skills_root.iterdir() if path.is_dir() and not path.name.startswith("_")):
    files = sorted(path.relative_to(skill_dir).as_posix() for path in skill_dir.rglob("*") if path.is_file())
    print(f"{skill_dir.name}: {', '.join(files)}")
print(f"SKILLS={sum(1 for path in skills_root.iterdir() if path.is_dir() and not path.name.startswith('_'))}")
