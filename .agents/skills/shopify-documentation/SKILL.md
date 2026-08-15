---
name: shopify-documentation
description: Audit or update Shopify theme documentation for setup, Shopify CLI usage, build steps, theme structure, merchant-facing configuration, validation, and release workflow. Use for README/docs tasks.
metadata:
  author: riley-childs
  version: "2.0"
---

# Focus

Document only workflows that exist in the repository. Prefer commands copied from package scripts/config over guessed setup steps. Keep README concise; move deep operational detail to focused docs only when needed.

# Workflow

1. Resolve the requested scope and outcome; widen it only for a necessary code dependency or behavior reason.
2. Inspect the target and only nearby files needed to verify behavior.
3. Load `references/checklist.md` only for deep or exhaustive audits.
4. For recursive audits, use `.agents/scripts/inventory.py`; do not claim full coverage without deterministic inventory.
5. Base findings on inspected code. If implementation is explicitly requested, make the smallest coherent change and preserve unrelated merchant-facing behavior.
6. Run relevant existing checks after edits when available.

# Output

- Lead with the highest-impact finding or action.
- Cite exact paths and code areas.
- Separate defects from optional improvements.
- Avoid restating standards the code already follows.
- After edits, list changed files and validation results.
