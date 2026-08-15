---
name: shopify-explain-code
description: Explain Shopify Liquid, JSON templates/schema, JavaScript/TypeScript, or CSS/SCSS code and how it participates in theme rendering/editor behavior. Use when the user asks how theme code works.
metadata:
  author: riley-childs
  version: "2.0"
---

# Focus

optimize for teaching rather than auditing. Explain the execution/rendering flow first, then key variables/objects, then any important Shopify-specific behavior. Mention concerns only when material to understanding the code.

# Workflow

1. Resolve the requested scope and outcome; widen it only for a necessary code dependency or behavior reason.
2. Inspect the target and only nearby files needed to verify behavior.
3. Load `references/checklist.md` only when Shopify-specific rendering/editor details need extra guidance.
4. Explain rendering/execution flow before implementation detail; inspect dependencies only when needed to explain behavior accurately.
5. Mention defects or improvements only when they materially help understanding.

# Output

- Lead with the highest-impact finding or action.
- Cite exact paths and code areas.
- Separate defects from optional improvements.
- Avoid restating standards the code already follows.
- After edits, list changed files and validation results.
