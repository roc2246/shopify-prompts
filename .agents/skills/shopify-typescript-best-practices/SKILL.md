---
name: shopify-typescript-best-practices
description: Review and refactor Shopify TypeScript for type safety, useful inference, narrowing, DOM correctness, API design, strictness, and maintainability without overengineering. Use for TypeScript audits/refactors.
metadata:
  author: riley-childs
  version: "2.0"
---

# Focus

Use the shared workflow/output. Inspect source TypeScript before generated JavaScript when both exist. Preserve runtime behavior unless behavior changes are requested. Prefer inference, narrow types, discriminated unions, type guards, and browser/Shopify-native APIs; add abstractions only when they remove duplication or encode a real invariant. Avoid `any`, unsafe assertions, redundant annotations, and type-level complexity that does not improve correctness.

# Workflow

See `.agents/skills/_base/common-workflow.md`.

# Output

See `.agents/skills/_base/common-output.md`.
