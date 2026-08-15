---
name: shopify-performance-review
description: Audit Shopify theme performance: Liquid render cost, asset loading, JavaScript/CSS weight, images/media, layout shifts, and third-party impact. Use for speed, Core Web Vitals, or performance-focused reviews.
metadata:
  author: riley-childs
  version: "2.0"
---

# Focus

Optimize measured or structurally clear bottlenecks first. Prefer HTML/CSS over JavaScript, defer noncritical work, and avoid speculative micro-optimizations that hurt clarity.

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
