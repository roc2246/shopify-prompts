# Shopify Theme Best Practices

Use these only when the task needs cross-cutting Shopify standards.

- Build around merchant-editable sections/blocks/settings instead of hard-coded content.
- Keep customization choices understandable; more settings are not automatically better.
- Prefer HTML/CSS and progressive enhancement; minimize JavaScript and blocking work.
- Use Shopify image/media primitives and responsive loading patterns.
- Keep Liquid render work simple and avoid redundant loops/lookups.
- Treat accessibility as a baseline requirement, not polish.
- Preserve localization and dynamic-source compatibility where relevant.
- Validate Liquid/JSON with Theme Check and use existing project lint/test/build tooling.
- Never edit `settings_data.json` casually: it can contain merchant configuration.
- Do not change established setting/block IDs without considering saved merchant data and migration impact.
