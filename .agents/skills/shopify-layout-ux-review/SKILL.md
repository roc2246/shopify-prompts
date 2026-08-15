---
name: shopify-layout-ux-review
description: Review Shopify storefront layout and UX for responsive behavior, accessibility, content hierarchy, merchant composition, conversion clarity, and production readiness. Use for layout, responsive, or UX audits.
metadata:
  author: riley-childs
  version: "2.0"
---

# Focus

Evaluate the rendered experience implied by the code. Do not invent visual defects that cannot be established from code/screenshots. Prioritize navigation, product/collection usability, forms, focus/keyboard behavior, mobile layout, and section-composition resilience.

# Workflow

1. Resolve the requested scope and outcome; widen it only for a necessary code dependency or behavior reason.
2. Inspect the target and only nearby files needed to verify behavior.
3. Load `references/checklist.md` only for deep or exhaustive audits.
4. For broad UX audits, inspect the relevant templates, sections, snippets, styles, scripts, and supplied screenshots; do not claim visual defects that cannot be established from evidence.
5. Base findings on inspected code. If implementation is explicitly requested, make the smallest coherent change and preserve unrelated merchant-facing behavior.
6. Run relevant existing checks after edits when available.

# Output

- Lead with the highest-impact finding or action.
- Cite exact paths and code areas.
- Separate defects from optional improvements.
- Avoid restating standards the code already follows.
- After edits, list changed files and validation results.
