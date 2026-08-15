# MERN → Shopify Workspace Migration

## Replaced

- Express/API/backend/business-logic skills → Shopify architecture, Liquid, section/block, and performance skills.
- React component/review skills → Shopify section/block and theme JS/TS skills.
- MERN test coverage → Shopify quality gates and risk-based test coverage.
- MERN standards → Shopify-native theme architecture and merchant/editor concerns.

## Token reductions

- Removed per-skill copies of project standards.
- Replaced large duplicated prompt files with one-line skill launchers.
- Reduced global instruction files to routing and invariants only.
- Kept deep criteria in optional `references/checklist.md`.
- Kept deterministic recursive inventory in scripts.

## Important semantic changes

- No mandatory approval gate is baked into every skill. Review-only requests remain read-only; explicit implementation requests can implement directly.
- Static Liquid is not forced into unit-test patterns. Theme Check and browser behavior checks are preferred where appropriate.
- Merchant schema/settings IDs are treated as compatibility contracts.
