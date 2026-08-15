---
name: shopify-scss-review
description: Review and refactor Shopify CSS/SCSS architecture for cascade safety, responsive behavior, useful Sass abstraction, duplication, and maintainability while preserving storefront appearance. Use for stylesheet audits/refactors.
metadata:
  author: riley-childs
  version: "2.0"
---

# Focus

Use the shared workflow/output. Inspect source SCSS before compiled CSS when both exist. Preserve rendered appearance unless redesign is requested. Use Sass variables/maps/functions/mixins only where they reduce repeated logic or encode a real design rule; do not convert plain CSS into ceremonial Sass.

# Workflow

See `.agents/skills/_base/common-workflow.md`.

# Output

See `.agents/skills/_base/common-output.md`.
