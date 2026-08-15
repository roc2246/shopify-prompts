# Shopify AI Dev Workspace

Lean, reusable Agent Skills for Shopify theme development.

## Goals

- Keep global AI context small.
- Load only the skill and references needed for the task.
- Favor Shopify-native solutions: Liquid, JSON templates, sections/blocks, snippets, theme settings, CSS/SCSS, and small progressive-enhancement JavaScript.
- Preserve merchant editor flexibility, accessibility, performance, and maintainability.
- Validate with existing project tooling, especially Shopify Theme Check when available.

## Structure

```text
.agents/skills/              Task-specific AI skills
  _base/                     Shared workflow/output rules
  shopify-*/                 Narrow Shopify skills
.github/copilot-instructions.md
prompts/                     Optional short launch prompts
architecture.md              Theme architecture conventions
coding-standards.md          Liquid/JS/TS/SCSS conventions
shopify-best-practices.md    Cross-cutting Shopify guidance
project-context.md           Generic project baseline
project-instructions.md      Lean global assistant rules
style-guide.md               Storefront UI conventions
```

## Recommended use

Ask the agent to use the narrowest matching skill and name the target files/folders.

Examples:

```text
Use shopify-liquid-review on sections/main-product.liquid. Focus on Liquid correctness and unnecessary work in loops.
```

```text
Use shopify-section-block to refactor sections/featured-collection.liquid. Preserve merchant settings and storefront behavior.
```

```text
Use shopify-scss-review on src/scss. Deep audit; preserve rendered appearance.
```

For implementation requests, the skill may edit directly when the user explicitly asks for changes. For review-only requests, do not mutate files.
