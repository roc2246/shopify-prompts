# Shared Workflow

1. Resolve the requested scope and outcome. Do not widen it without a code dependency or behavior reason.
2. Inspect the target and only nearby files needed to verify behavior.
3. Read root standards only when repository conventions affect the answer.
4. For deep/exhaustive audits, read this skill's `references/checklist.md`.
5. For recursive audits, use `scripts/inventory.py` when present.
6. Base findings on inspected code; do not claim full coverage without an inventory.
7. If the user asks to implement, make the smallest coherent change, preserve unrelated behavior, then run relevant existing checks.
