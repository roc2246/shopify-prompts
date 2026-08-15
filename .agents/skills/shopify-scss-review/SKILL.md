---
name: shopify-scss-review
description: Review and refactor Shopify CSS/SCSS architecture for cascade safety, responsive behavior, useful Sass abstraction, duplication, and maintainability while preserving storefront appearance. Use for stylesheet audits/refactors.
metadata:
  author: riley-childs
  version: "2.0"
---

# Focus

Inspect source SCSS before compiled CSS when both exist. Preserve rendered appearance unless redesign is requested. Use Sass variables/maps/functions/mixins only where they reduce repeated logic or encode a real design rule; do not convert plain CSS into ceremonial Sass.

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
