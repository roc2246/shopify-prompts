# Agent Skills

Use `.agents/skills/` as the task interface.

## Design rules

1. Select the narrowest skill by `name` + `description`.
2. Load only that `SKILL.md` first.
3. Read root standards only when repository conventions matter.
4. Read `references/checklist.md` only for deep/exhaustive audits.
5. Use scripts for deterministic inventory instead of asking the model to remember every file.
6. Keep prompts thin; do not duplicate skill instructions in `.prompt.md` files.
7. Prefer evidence from inspected code over generic advice.
8. Do not broaden scope unless dependencies or runtime behavior require it.

This progressive-disclosure design minimizes context-window usage while retaining detailed guidance when needed.
