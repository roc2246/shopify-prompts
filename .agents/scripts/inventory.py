#!/usr/bin/env python3
"""Deterministically inventory Shopify theme source files."""

import argparse
from pathlib import Path

DEFAULT_EXCLUDES = {
    ".git", "node_modules", "dist", "build", ".shopify", "coverage",
    ".cache", ".vite", ".turbo"
}

parser = argparse.ArgumentParser(description="Deterministic Shopify theme source inventory")
parser.add_argument("root", nargs="?", default=".")
parser.add_argument("--ext", nargs="+", default=[".liquid", ".json", ".js", ".ts", ".css", ".scss"])
parser.add_argument("--exclude", nargs="*", default=[], help="Additional directory names to exclude")
args = parser.parse_args()
root = Path(args.root)
exts = {extension if extension.startswith(".") else f".{extension}" for extension in args.ext}
ignore = DEFAULT_EXCLUDES | set(args.exclude)
items = sorted(
    path for path in root.rglob("*")
    if path.is_file() and path.suffix in exts and not any(part in ignore for part in path.parts)
)
for path in items:
    print(path.as_posix())
print(f"TOTAL={len(items)}")
