#!/usr/bin/env python3
import argparse
from pathlib import Path

p=argparse.ArgumentParser(description="Deterministic source inventory")
p.add_argument("root", nargs="?", default=".")
p.add_argument("--ext", nargs="+", default=[".liquid", ".json", ".js", ".ts", ".css", ".scss"])
a=p.parse_args()
root=Path(a.root)
exts={e if e.startswith(".") else f".{e}" for e in a.ext}
ignore={".git", "node_modules", "dist", "build", ".shopify"}
items=sorted(x for x in root.rglob("*") if x.is_file() and x.suffix in exts and not any(part in ignore for part in x.parts))
for x in items: print(x.as_posix())
print(f"TOTAL={len(items)}")
