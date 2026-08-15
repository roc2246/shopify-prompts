---
name: shopify-js-ts-review
description: Review Shopify theme browser behavior in JavaScript or TypeScript for progressive enhancement, DOM safety, theme-editor lifecycle handling, accessibility, performance, and event/state management. Use when runtime storefront behavior is the focus; use shopify-typescript-best-practices when the primary question is TypeScript type design or type safety.
metadata:
  author: riley-childs
  version: "2.0"
---

# Focus

Prefer browser/Shopify-native APIs and minimal client state. Verify DOM assumptions, listener cleanup/delegation, multiple section instances, and section editor re-rendering when relevant. For TypeScript, focus on useful safety rather than maximizing annotations.

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
