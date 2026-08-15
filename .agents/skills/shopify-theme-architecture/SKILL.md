---
name: shopify-theme-architecture
description: Audit Shopify theme structure and responsibility boundaries across layouts, templates, section groups, sections, blocks, snippets, config, locales, and assets. Use for architecture, organization, or full-theme structure reviews.
metadata:
  author: riley-childs
  version: "2.0"
---

# Focus

Prefer standard Shopify directories and merchant-composable JSON templates/section groups where appropriate. Flag architecture only when it causes duplication, editor friction, coupling, or unsafe change risk.

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
