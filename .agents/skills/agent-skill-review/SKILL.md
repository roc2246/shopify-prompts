---
name: agent-skill-review
description: Audit Agent Skills for reliable activation, progressive disclosure, token efficiency, portability, deterministic tooling, and unnecessary duplication. Use when reviewing or optimizing `.agents/skills/` architecture.
metadata:
  author: riley-childs
  version: "1.0"
---

# Focus

Evaluate skills as reusable agent capabilities rather than long prompts. Prefer narrow discoverable metadata, concise always-loaded instructions, optional references, deterministic scripts for mechanical work, and self-contained portability.

# Workflow

1. Inventory every skill and its files.
2. Check `name` and `description` for clear task matching and non-overlapping scope.
3. Keep `SKILL.md` limited to instructions needed whenever the skill activates.
4. Move deep domain guidance to references and load it only when required.
5. Prefer scripts for deterministic inventory or repeatable mechanical work.
6. Flag stale paths, missing referenced files, generated artifacts, legacy prompt duplicates, and hidden cross-skill dependencies.
7. Recommend changes only when they improve reliability, portability, or context efficiency.

For package inventory, run `python ./.agents/scripts/inventory-skills.py .` before making full-coverage claims.

# Output

Lead with structural defects, then skill-specific improvements. Distinguish required fixes from optional optimization. After edits, validate metadata, references, scripts, and stale paths.
