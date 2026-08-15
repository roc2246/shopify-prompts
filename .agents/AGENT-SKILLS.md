# Shopify Agent Skills

`.agents/skills/` is the task interface for this portable Shopify AI package.

## Progressive-disclosure rules

1. Match the request to the narrowest skill using its YAML `name` and `description`.
2. Load only that skill's `SKILL.md` first.
3. Load its `references/checklist.md` only when deeper audit guidance is required.
4. Use `scripts/inventory.py` for recursive completeness claims when the skill provides it.
5. Use `.agents/docs/` only when cross-cutting Shopify/project standards materially affect the task.
6. Do not preload every skill or documentation file.
7. Prefer inspected project evidence over generic Shopify advice.

Tool-specific adapters live under `.agents/adapters/` and should remain thin routers into this skill package.
