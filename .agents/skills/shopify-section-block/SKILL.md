---
name: shopify-section-block
description: Build or refactor Shopify sections, theme blocks, snippets, and schema for merchant-configurable storefront features. Use when creating or restructuring a section/block or its settings.
metadata:
  author: riley-childs
  version: "2.0"
---

# Focus

Preserve existing setting/block IDs unless migration is intentional. Keep schema small and understandable, provide sensible defaults, use blocks only when merchants benefit from repeatable/reorderable content, and keep rendering accessible without JavaScript when practical.

When implementing, include schema and related asset changes only when needed.

# Workflow

1. Resolve the requested scope and outcome; widen it only for a necessary code dependency or behavior reason.
2. Inspect the target and only nearby files needed to verify behavior.
3. Load `references/checklist.md` only for deep or exhaustive audits.
4. For recursive audits, use `scripts/inventory.py` when present; do not claim full coverage without deterministic inventory.
5. Base findings on inspected code. If implementation is explicitly requested, make the smallest coherent change and preserve unrelated merchant-facing behavior.
6. Run relevant existing checks after edits when available.

# Output

- Lead with the highest-impact finding or action.
- Cite exact paths and code areas.
- Separate defects from optional improvements.
- Avoid restating standards the code already follows.
- After edits, list changed files and validation results.
