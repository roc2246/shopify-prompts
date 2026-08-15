---
name: shopify-test-quality
description: Audit Shopify theme quality checks and test coverage, including Theme Check, lint/build validation, storefront interaction tests, and unit tests for nontrivial JS/TS when a test framework exists. Use for test/quality-gate requests.
metadata:
  author: riley-childs
  version: "2.0"
---

# Focus

Do not demand unit tests for static Liquid markup by default. Match tests to failure risk: Theme Check for Liquid/JSON, browser/interaction coverage for storefront behavior, and unit tests for nontrivial pure JS/TS logic when the project supports them.

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
