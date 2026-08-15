---
name: shopify-typescript-best-practices
description: Review Shopify TypeScript primarily for type safety, inference, narrowing, DOM typing, API/type design, strictness, and maintainable type modeling without overengineering. Use when TypeScript itself is the focus; use shopify-js-ts-review for storefront runtime behavior, lifecycle, events, or progressive enhancement.
metadata:
  author: riley-childs
  version: "2.0"
---

# Focus

Inspect source TypeScript before generated JavaScript when both exist. Preserve runtime behavior unless behavior changes are requested. Prefer inference, narrow types, discriminated unions, type guards, and browser/Shopify-native APIs; add abstractions only when they remove duplication or encode a real invariant. Avoid `any`, unsafe assertions, redundant annotations, and type-level complexity that does not improve correctness.

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
