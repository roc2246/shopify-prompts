#!/usr/bin/env python3
import argparse
from pathlib import Path

DEFAULT_EXCLUDES = {
    ".git", "node_modules", "dist", "build", ".shopify", "coverage",
    ".cache", ".vite", ".turbo"
}

p = argparse.ArgumentParser(description="Deterministic Shopify theme source inventory")
p.add_argument("root", nargs="?", default=".")
p.add_argument("--ext", nargs="+", default=[".liquid", ".json", ".js", ".ts", ".css", ".scss"])
p.add_argument("--exclude", nargs="*", default=[], help="Additional directory names to exclude")
a = p.parse_args()
root = Path(a.root)
exts = {e if e.startswith(".") else f".{e}" for e in a.ext}
ignore = DEFAULT_EXCLUDES | set(a.exclude)
items = sorted(
    x for x in root.rglob("*")
    if x.is_file() and x.suffix in exts and not any(part in ignore for part in x.parts)
)
for x in items:
    print(x.as_posix())
print(f"TOTAL={len(items)}")
