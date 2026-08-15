# TypeScript Checklist

- Source/generated boundary understood
- `strict` compiler settings used when project-compatible
- Inference preferred over redundant annotations
- `unknown` + narrowing preferred over `any`
- Assertions minimized; DOM elements narrowed safely
- Null/undefined and optional values handled explicitly
- Unions/discriminated unions model real states
- Type guards and predicates are correct and useful
- Public functions/events/data shapes have clear types
- Generics add reuse or safety, not abstraction for its own sake
- `readonly`, literal types, `as const`, and `satisfies` used only where they preserve useful invariants
- Shopify section instances/editor lifecycle do not rely on unsafe global assumptions
- Browser and Shopify-native APIs preferred over custom type-heavy wrappers
- Runtime validation exists when external/untrusted data crosses a type boundary
- No dead types, duplicate interfaces, broad index signatures, or unnecessary enums
