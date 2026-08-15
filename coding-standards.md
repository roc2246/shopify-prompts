# Coding Standards

## Liquid
- Prefer clear `assign`, `capture`, `render`, and simple conditionals over dense expressions.
- Use `{% render %}` for snippets and pass only needed values.
- Avoid repeated expensive work inside loops.
- Escape merchant/user text unless intentionally rendering trusted HTML.
- Keep schema IDs stable once merchants may have saved settings.
- Use translation keys for reusable storefront strings when localization matters.

## HTML
- Use semantic elements, valid labels, keyboard-accessible controls, and meaningful image alt behavior.
- Do not replace native controls with div-based interactions without necessity.

## JavaScript / TypeScript
- Progressive enhancement first.
- Small modules; minimal globals; event delegation where useful.
- Handle Shopify section/block lifecycle events when code must survive theme-editor re-rendering.
- Avoid libraries for behavior the platform/browser already provides.
- In TypeScript, type DOM queries and public/shared boundaries; avoid decorative types.

## CSS / SCSS
- Mobile first.
- Keep selectors shallow and component/section scoped.
- Reuse tokens, functions, and mixins only when they remove meaningful duplication.
- Avoid over-nesting and abstraction for one-off values.
- Keep compiled assets out of source reviews when source files exist.
