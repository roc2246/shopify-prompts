# Shopify Theme Architecture

Prefer Shopify's standard theme directories:

```text
assets/
blocks/
config/
layout/
locales/
sections/
snippets/
templates/
```

Optional source/tooling directories such as `src/`, `scripts/`, or `tests/` may exist when the project compiles assets before Shopify upload.

## Responsibilities

- `layout/`: document shell and shared page chrome.
- `templates/`: page composition, preferably JSON where supported.
- `sections/`: merchant-configurable page regions.
- `blocks/`: reusable merchant-configurable theme blocks when the theme uses them.
- `snippets/`: reusable Liquid rendering fragments without section schema.
- `config/`: global theme settings and saved setting data.
- `locales/`: storefront/editor translations.
- `assets/`: browser-delivered theme assets and compiled output.

Keep dependencies one-way where practical: templates compose sections; sections/blocks render snippets; snippets should not become hidden application controllers.
